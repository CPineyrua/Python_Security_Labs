import hashlib
import sys
import json
import os

# Colores para la terminal
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BLUE = "\033[94m"

DATABASE = "integrity_db.json"

def get_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def save_integrity(file_path, file_hash):
    # Cargamos la base de datos actual o creamos una nueva
    data = {}
    if os.path.exists(DATABASE):
        with open(DATABASE, "r") as f:
            data = json.load(f)
    
    data[file_path] = file_hash
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"{BLUE}[i] Hash guardado en '{DATABASE}' para futuras verificaciones.{RESET}")

def verify_integrity(file_path):
    if not os.path.exists(DATABASE):
        print(f"{RED}[!] No hay base de datos de integridad. Registra el archivo primero.{RESET}")
        return

    with open(DATABASE, "r") as f:
        data = json.load(f)

    if file_path not in data:
        print(f"{RED}[!] El archivo '{file_path}' no está registrado.{RESET}")
        return

    original_hash = data[file_path]
    current_hash = get_file_hash(file_path)

    print(f"\n--- Verificación Automática: {file_path} ---")
    if current_hash == original_hash:
        print(f"Estado: {GREEN}✔ INTEGRITY OK{RESET}")
    else:
        print(f"Estado: {RED}✘ FILE COMPROMISED{RESET}")
        print(f"Hash esperado (Guardado): {original_hash}")
        print(f"Hash actual (Calculado): {current_hash}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("\n[!] Uso Profesional:")
        print(f"    Registrar archivo:  python file_integrity.py register <archivo>")
        print(f"    Verificar archivo:  python file_integrity.py verify <archivo>")
    else:
        command = sys.argv[1].lower()
        file_name = sys.argv[2]

        if command == "register":
            h = get_file_hash(file_name)
            if h:
                print(f"Registrando: {file_name}")
                print(f"Hash: {h}")
                save_integrity(file_name, h)
            else:
                print(f"{RED}[!] Error: No se pudo leer el archivo.{RESET}")
        
        elif command == "verify":
            verify_integrity(file_name)