# Escáner de Puertos con Python

## Índice 📖
1. [Intro](https://github.com/KamVilchis/python-port-scanner#1-intro-)
2. [Qué construí](https://github.com/KamVilchis/python-port-scanner#2-qu%C3%A9-constru%C3%AD-)
3. [Objetivo del proyecto](https://github.com/KamVilchis/python-port-scanner#3-objetivo-del-proyecto-)
4. [Cómo ejecutarlo](https://github.com/KamVilchis/python-port-scanner#4-c%C3%B3mo-ejecutarlo-)
5. [Ejemplo de salida](https://github.com/KamVilchis/python-port-scanner#5-ejemplo-de-salida-)
6. [Nota importante](https://github.com/KamVilchis/python-port-scanner#%EF%B8%8F-nota-importante)

## 1. Intro 😎

Python es un lenguaje muy versátil que permite trabajar con redes utilizando librerías integradas como `socket`.

En este proyecto desarrollé un escáner de puertos que permite identificar qué puertos están abiertos en una dirección IP específica y, si es posible, capturar el banner del servicio que está corriendo en ese puerto.

## 2. Qué construí 🙌

En este proyecto desarrollé un script llamado `scanner.py` que:

* Escanea un rango de puertos definido por el usuario.
* Verifica cuáles puertos están abiertos.
* Intenta capturar el banner del servicio activo.
* Muestra los resultados en consola.

El escaneo se realiza usando sockets TCP (`AF_INET`, `SOCK_STREAM`) y la función `connect_ex()` para verificar la conexión.

## 3. Objetivo del proyecto 🎯

* Comprender cómo funcionan las conexiones TCP.
* Aprender a utilizar la librería `socket` en Python.
* Entender el concepto de puertos abiertos y servicios en red.
* Aplicar conceptos básicos de ciberseguridad y redes.

## 4. Cómo ejecutarlo ⚡

### Requisitos
* Tener instalado **Python 3**.
* No se necesitan librerías externas.

### Pasos para ejecutarlo

1. Clona el repositorio:

```bash
git clone https://github.com/KamVilchis/python-port-scanner.git
```

2. Entra a la carpeta del proyecto:

```bash
cd ~/python-port-scanner
```

3. Abre `scanner.py` y modifica las variables para ajustarlas a tus necesidades:

* **ip_objetivo** → Cambia la IP del host que deseas escanear.
* **puerto_inicio** y **puerto_fin** → Define el rango de puertos que quieres escanear.

4. Ejecuta el script:

```bash
python scanner.py
```

## 5. Ejemplo de salida 💻

```bash
[+] Puerto 21: ABIERTO
    ↳ Banner: 220 (vsFTPd 2.3.4)

[+] Puerto 22: ABIERTO
    ↳ Banner: SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
```

## ⚠️ Nota importante

Este proyecto fue desarrollado con fines educativos.

Debe utilizarse únicamente en redes y sistemas donde tengas autorización para realizar pruebas.

