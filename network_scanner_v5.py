import socket
import sys
from ipaddress import ip_address
from datetime import datetime

def log_result(message):
    with open("scan_report.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

def check_service(ip_str, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            result = s.connect_ex((ip_str, port))
            if result == 0:
                try: service = socket.getservbyport(port)
                except: service = "unknown"
                msg = f"[+] {ip_str}:{port} is OPEN ({service})"
            else:
                msg = f"[-] {ip_str}:{port} is CLOSED"
            print(msg)
            log_result(msg)
    except Exception as e:
        print(f"[-] Error en puerto {port}: {e}")

if __name__ == "__main__":
    # Validamos que tengamos al menos la IP y la definición de puertos
    if len(sys.argv) != 3:
        print("\n[!] Uso profesional:")
        print("    Rango: python network_scanner_v5.py <IP> 20-80")
        print("    Lista: python network_scanner_v5.py <IP> 22,80,443\n")
        sys.exit(1)

    target_input = sys.argv[1]
    ports_input = sys.argv[2]

    try:
        target_ip = str(ip_address(target_input.strip()))
        ports_to_scan = []

        # LÓGICA DE DETECCIÓN: ¿Rango o Lista?
        if "-" in ports_input:
            # Es un rango (ej: 20-25)
            start, end = map(int, ports_input.split("-"))
            ports_to_scan = list(range(start, end + 1))
        elif "," in ports_input:
            # Es una lista (ej: 22,80,443)
            ports_to_scan = [int(p) for p in ports_input.split(",")]
        else:
            # Es un solo puerto
            ports_to_scan = [int(ports_input)]

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_result(f"\n--- Advanced Scan: {target_ip} | {timestamp} ---")
        
        print(f"\nIniciando escaneo en {target_ip} ({len(ports_to_scan)} puertos)...")
        print("-" * 45)

        for port in ports_to_scan:
            check_service(target_ip, port)

    except ValueError:
        print("\n[!] Error: Formato de puertos incorrecto. Usa '20-80' o '22,80,443'.")
    except KeyboardInterrupt:
        print("\n[!] Escaneo abortado.")