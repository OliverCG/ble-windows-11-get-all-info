import subprocess,os,zipfile,sys,importlib,argparse

def argumentos_linea_comando():
    parser = argparse.ArgumentParser(description="Script para obtener información de conexión de dispositivos BLE emparejados usando PsExec")
    parser.add_argument("--ayuda", help="Muestra este mensaje de ayuda", action="store_true")
    parser.add_argument("--sigilo", help="Elimina todo rastro de ejecutables", action="store_true")
    return parser.parse_args()

# Obtenemos los argumentos
args = argumentos_linea_comando()

if args.ayuda:
    print("""
    Uso: BleGetAllInfo.py [OPCIONES]
    
    OPCIONES:
      --ayuda    Muestra este mensaje de ayuda.
      --sigilo   Elimina todo rastro de ejecutables.
    
    Descripción: Este script utiliza PsExec para extraer información de dispositivos BLE emparejados en un sistema Windows 11 Pro.
    """)
    exit()

def instalar_paquete(nombre):
    subprocess.check_call([sys.executable, "-m", "pip", "install", nombre])
    importlib.invalidate_caches()  # invalidar la caché del buscador de módulos

def importar_o_instalar(nombre):
    try:
        return importlib.import_module(nombre)
    except ImportError:
        print(f"El módulo '{nombre}' no está instalado. Instalándolo ahora...")
        instalar_paquete(nombre)
        return importlib.import_module(nombre)

# Usar la función para importar requests
requests = importar_o_instalar('requests')

# Variables globales como el directorio de salida para PsExec.exe y ficheros resultantes
output_directory = os.getcwd()
psexec = "PsExec.exe"
pstools = "PsTools.zip"
bt_devices = "bt_devices.txt"
bt_keys = "bt_keys.txt"
current_file = "BleGetAllInfo.py"
psexec_path = os.path.join(output_directory, psexec)
bt_devices_path = os.path.join(output_directory, bt_devices)
bt_keys_path = os.path.join(output_directory, bt_keys)
current_file_path = os.path.join(output_directory, current_file)

# URL de descarga de PsTools (donde se encuentra PsExec.exe)
psexec_url = "https://download.sysinternals.com/files/PSTools.zip"


def descargar_y_extraer_psexec(url, output_dir):
    zip_path = os.path.join(output_dir, pstools)

    # Descargar el archivo ZIP
    print("Descargando PsTools...")
    response = requests.get(url)
    with open(zip_path, 'wb') as file:
        file.write(response.content)

    # Extraer PsExec.exe del ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        print("Extrayendo PsExec.exe...")
        zip_ref.extract("PsExec.exe", path=output_dir)

    # Eliminar el archivo ZIP
    os.remove(zip_path)
    print("Archivo PsTools.zip eliminado.")

def ejecutar_psexec(reg_path, output_file):
    command = f"{psexec_path} -s -i regedit /E {os.getcwd()}\\{output_file} \"{reg_path}\""
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.stderr:
        print("Error:", result.stderr.decode())
    else:
        print(f"{output_file} generado correctamente.")

if not os.path.exists(psexec_path):
    descargar_y_extraer_psexec(psexec_url, output_directory)

# Rutas de los registros
reg_bluetooth_devices = "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\BTHPORT\\Parameters\\Devices"
reg_bluetooth_keys = "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\BTHPORT\\Parameters\\Keys"

# Eliminar los archivos si existieran
if os.path.exists(bt_devices_path):
    os.remove(bt_devices_path)
    print(f"The file {bt_devices_path} has been deleted.")
if os.path.exists(bt_keys_path):
    os.remove(bt_keys_path)
    print(f"The file {bt_keys_path} has been deleted.")

# Ejecutar comandos
ejecutar_psexec(reg_bluetooth_devices, bt_devices)
ejecutar_psexec(reg_bluetooth_keys, bt_keys)

if args.sigilo:
    print("Modo sigiloso activado.")
    # Eliminar rastro de PsExec
    if os.path.exists(psexec_path):
        os.remove(psexec_path)
        print(f"The file {psexec_path} has been deleted.")

    # Eliminar rastro del archivo actual
    if os.path.exists(current_file_path):
        os.remove(current_file_path)
        print(f"The file {current_file_path} has been deleted.")
