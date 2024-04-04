# Extraer información de un dispositivo BLE emparejado con Windows 11 Pro

## Descripción

Este script en Python, `BleGetAllInfo.py`, está diseñado para extraer información detallada de dispositivos Bluetooth Low Energy (BLE) emparejados en un sistema operativo Windows 11 Pro. Utiliza la herramienta `PsExec.exe` de Microsoft para acceder al registro del sistema y extraer claves y servicios relacionados con dispositivos BLE.

## Características

- Extracción de información del registro sobre dispositivos BLE emparejados.
- Generación de archivos `bt_keys` y `bt_devices` con la información del dispositivo extraída del registro de Windows.

## Requisitos

- Python 3.x
- Acceso a Internet para la descarga de `PsExec.exe` de Microsoft Sysinternals.
- Privilegios de administrador en el sistema Windows 11 Pro donde se ejecutará el script.

## Instalación y Ejecución

1. Clone el repositorio o descargue el script `BleGetAllInfo.py`.
2. Asegúrese de que Python 3.x esté instalado en su sistema.
3. Ejecute el script en una terminal o línea de comandos con permisos de administrador: `python BleGetAllInfo.py`
4. El script descargará automáticamente `PsExec.exe` y realizará las operaciones necesarias para generar los archivos `bt_keys` y `bt_devices`.

## Funcionamiento

El script realiza los siguientes pasos:

1. Descarga `PsExec.exe` si no está presente en el sistema.
2. Ejecuta comandos para extraer información del registro de Windows relacionada con dispositivos BLE emparejados.
3. Genera los diferentes archivos con el volcado de la información.

## Autoría

Oliver Calvo García

Este proyecto ha sido desarrollado por Oliver Calvo García, un apasionado ingeniero de software con experiencia en el desarrollo de aplicaciones web y herramientas de seguridad informática. Más información en su web: https://olivercg.es
