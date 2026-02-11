import datetime

# Abrimos el archivo de logs
with open('servidor.log', 'r') as archivo:
    intentos_fallidos = {}

    for linea in archivo:
        # Buscamos solo las líneas que tienen fallos
        if "LOGIN_FAILED" in linea:
            # Extraemos la IP (la primera parte de la línea)
            ip = linea.split(" - ")[0]
            # Contamos el fallo
            intentos_fallidos[ip] = intentos_fallidos.get(ip, 0) + 1

    # Revisamos los resultados
    for ip, cuenta in intentos_fallidos.items():
        ahora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if cuenta > 3:
            print(f"\033[91m[{ahora}] 🚨 ALERTA DE SEGURIDAD: La IP {ip} intentó entrar {cuenta} veces.\033[0m")
        else:
            print(f"\033[92m[{ahora}] Info: IP {ip} tiene {cuenta} intentos fallidos (Bajo control).\033[0m")