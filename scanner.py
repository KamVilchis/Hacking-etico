import socket

ip_objetivo = '192.168.61.129'
puerto_inicio = 1
puerto_fin = 200

for puerto in range(puerto_inicio, puerto_fin + 1):
    try:
        socket_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_conexion.settimeout(3)

        resultado = socket_conexion.connect_ex((ip_objetivo, puerto))
        if resultado == 0:
            print(f"[+] Puerto {puerto}: ABIERTO")

            try:
                banner = socket_conexion.recv(1024)
                banner_texto = banner.decode('utf-8', errors='ignore')


                if banner_texto:
                        print(f"    ↳ Banner: {banner_texto}")
                else:
                    print("    ↳ Banner: No recibido")

            except:
                print("    ↳ Banner: No se pudo capturar")

        socket_conexion.close()

    except:
        print(f"[!] Error al escanear el puerto {puerto}")
