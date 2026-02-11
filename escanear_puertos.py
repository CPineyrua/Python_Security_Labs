"""
Escaner simple de puertos 80 y 443 usando socket.
Explicado para examen de redes.
"""

import socket

# IP a escanear (cámbiala por la que quieras probar)
IP = "127.0.0.1"

# Puertos a comprobar: 80 (HTTP) y 443 (HTTPS)
PUERTOS = [80, 443]


def puerto_abierto(ip, puerto, timeout=2):
    """
    Intenta conectar por TCP al puerto dado.
    Si la conexión se establece, el puerto está abierto.
    """
    # Crear un socket de tipo AF_INET (IPv4) y SOCK_STREAM (TCP)
    # TCP es orientado a conexión: handshake de 3 pasos antes de enviar datos
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Timeout en segundos: si no hay respuesta en ese tiempo, se considera cerrado
    # Evita que el programa se quede colgado esperando
    sock.settimeout(timeout)

    try:
        # connect() intenta establecer la conexión TCP con el servidor
        # Si el puerto está abierto y hay un servicio escuchando, la conexión se completa
        # Si está cerrado o filtrado, se lanzará una excepción (ConnectionRefusedError, etc.)
        sock.connect((ip, puerto))
        return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        # timeout: no hubo respuesta (puerto filtrado o host inalcanzable)
        # ConnectionRefusedError: el puerto está cerrado (RST del destino)
        # OSError: otros errores de red (ej. host no encontrado)
        return False
    finally:
        # Cerrar el socket para liberar el recurso del sistema
        sock.close()


def main():
    print(f"Escaneando {IP} - Puertos 80 (HTTP) y 443 (HTTPS)\n")

    for puerto in PUERTOS:
        if puerto_abierto(IP, puerto):
            print(f"  Puerto {puerto}: ABIERTO  (hay un servicio escuchando)")
        else:
            print(f"  Puerto {puerto}: CERRADO o FILTRADO")


if __name__ == "__main__":
    main()
