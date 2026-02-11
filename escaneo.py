import socket

def escanear():
    # Pedimos la IP al usuario
    target = input("Ingrese la IP que desea escanear (ejemplo 8.8.8.8): ")
    puertos = [80, 443]

    for puerto in puertos:
        # Creamos el socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2) # Damos 2 segundos de margen
        
        try:
            # Intentamos conectar
            result = sock.connect_ex((target, puerto))
            
            if result == 0:
                print(f"✅ El puerto {puerto} está ABIERTO en {target}")
            else:
                print(f"❌ El puerto {puerto} está CERRADO en {target}")
                
        except Exception as e:
            print(f"⚠️ Error al escanear puerto {puerto}: {e}")
        
        finally:
            # Esto siempre se ejecuta, cerrando la conexión de forma segura
            sock.close()

if __name__ == "__main__":
    escanear()