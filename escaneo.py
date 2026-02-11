import socket
from ipaddress import ip_address
from datetime import datetime  # Para saber CUÁNDO ocurrió el escaneo

def log_result(message):
    """Guarda el resultado en un archivo de texto de forma segura."""
    with open("scan_report.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

def check_service(ip_str, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            result = s.connect_ex((ip_str, port))
            
            # Preparamos el mensaje
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                msg = f"[+] {ip_str}:{port} is OPEN ({service})"
            else:
                msg = f"[-] {ip_str}:{port} is CLOSED"
            
            # Imprimimos en pantalla Y guardamos en el log
            print(msg)
            log_result(msg)
            
    except Exception as e:
        error_msg = f"[-] Error en puerto {port}: {e}"
        print(error_msg)
        log_result(error_msg)

if __name__ == "__main__":
    print("--- Professional Port Scanner v3 (With Logging) ---")
    u_input = input("Introduce la IP a escanear: ")
    
    try:
        target_ip = str(ip_address(u_input.strip()))
        start_p = int(input("Puerto inicio: "))
        end_p = int(input("Puerto fin: "))
        
        # Cabecera del reporte con fecha y hora
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"\n--- Scan Report: {target_ip} | {timestamp} ---"
        log_result(header)
        
        print(f"\nEscaneando... (Resultados guardados en scan_report.txt)")
        print("-" * 45)
        
        for port in range(start_p, end_p + 1):
            check_service(target_ip, port)
            
    except ValueError:
        print("\n[!] Error: Datos inválidos.")
    except KeyboardInterrupt:
        print("\n[!] Escaneo detenido.")