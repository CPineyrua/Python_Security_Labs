import requests
import sys

# Colores para el diagnóstico
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BLUE = "\033[94m"

def check_headers(url):
    if not url.startswith("http"):
        url = "https://" + url

    print(f"\n{BLUE}--- Auditoría de Seguridad Web: {url} ---{RESET}\n")

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        
        # 1. Banner Grabbing (Detección de Servidor)
        server = headers.get("Server", "Oculto o No detectado")
        print(f"{BLUE}[i] Servidor detectado: {server}{RESET}\n")

        # 2. Análisis de Cabeceras
        security_headers = {
            "X-Frame-Options": "Protege contra Clickjacking.",
            "Content-Security-Policy": "Previene inyección de scripts (XSS).",
            "Strict-Transport-Security": "Fuerza el uso de HTTPS (HSTS).",
            "X-Content-Type-Options": "Evita el sniffing de tipo MIME."
        }

        score = 0
        for header, description in security_headers.items():
            if header in headers:
                print(f"{GREEN}[✔] {header:25} PRESENTE{RESET}")
                score += 1
            else:
                print(f"{RED}[✘] {header:25} AUSENTE{RESET}")
        
        # 3. Sistema de Puntuación Profesional
        print(f"\n{BLUE}--- Resumen de Seguridad ---{RESET}")
        if score == 4:
            print(f"Puntuación: {GREEN}{score}/4 (Excelente){RESET}")
        elif score >= 2:
            print(f"Puntuación: {YELLOW}{score}/4 (Media - Requiere mejoras){RESET}")
        else:
            print(f"Puntuación: {RED}{score}/4 (CRÍTICA - Vulnerable){RESET}")

    except Exception as e:
        print(f"{RED}[!] Error de conexión: {e}{RESET}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\n[!] Uso: python web_security_scanner.py <url>")
    else:
        check_headers(sys.argv[1])