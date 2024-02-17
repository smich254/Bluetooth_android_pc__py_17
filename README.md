# Título: Programa para recibir datos por Bluetooth

## Descripción:

Este programa permite recibir datos por Bluetooth desde un dispositivo Android.

## Requisitos:

- Python 3.5 o superior
- Librería PyBluez
- Librería PyQt5
- Un dispositivo Android con Bluetooth activado

## Configuración del entorno virtual:

1. Instalar virtualenv o venv (Python 3).
2. Crear un entorno virtual:
```
python -m venv venv
```
3. Activar el entorno virtual:
```
venv\Scripts\activate
```

## Instalación de librerías:

1. Activar el entorno virtual.
2. Instalar las librerías:
```
pip install pybluez PyQt5
```

## Uso del software:

1. Asegúrate de que el dispositivo Android esté visible para Bluetooth.
2. Ejecuta el programa:
```
python recibir_datos_bluetooth.py
```
3. Selecciona el dispositivo Android de la lista.
4. Haz clic en "Conectar".
5. El programa mostrará los datos que se reciban del dispositivo Android.

## Nota:

- Este programa es un ejemplo básico y puede ser modificado para agregar más funcionalidades.
- Puedes encontrar más información sobre PyBluez en la siguiente página: https://pybluez.readthedocs.io/en/latest/
- Puedes encontrar más información sobre PyQt5 en la siguiente página: https://www.riverbankcomputing.com/software/pyqt/
