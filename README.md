# Python Security Labs 🛡️

Español | [English](#english)

## 🇪🇸 Español

Este repositorio es un ecosistema de herramientas profesionales desarrolladas en Python para la automatización de tareas de ciberseguridad, abarcando desde el análisis de redes hasta la forense digital y auditoría web.

### 🛠️ Laboratorios Disponibles

#### 1. Network Scanner (v5 - Professional CLI)
Escáner de puertos avanzado que utiliza el protocolo TCP para identificar servicios activos.
* **Capacidades:** Soporta escaneo por rangos (`20-80`) y listas específicas (`22,80,443`).
* **Conceptos:** Automatización de CLI con `sys.argv`, validación de IPs y manejo de sockets.
* **Uso:** `python network_scanner_v5.py 127.0.0.1 20-443`

#### 2. Integrity Manager (IDS Simulado)
Sistema de detección de integridad basado en criptografía para proteger archivos contra manipulaciones.
* **Capacidades:** Registro de huellas digitales (SHA-256) y verificación automática con persistencia en JSON.
* **Conceptos:** Criptografía aplicada (`hashlib`), persistencia de datos y alertas visuales ANSI (Rojo/Verde).
* **Uso:** `python file_integrity.py register archivo.txt` o `verify archivo.txt`

#### 3. Web Security Auditor
Scanner de vulnerabilidades en cabeceras HTTP para evaluar la postura de seguridad de aplicaciones web.
* **Capacidades:** Detección de Banner Grabbing (servidor) y sistema de puntuación (Scoring 0/4).
* **Conceptos:** Protocolo HTTP, análisis de cabeceras de seguridad (CSP, HSTS, XFO) y auditoría de riesgos.
* **Uso:** `python web_security_scanner.py google.com`

---

<a name="english"></a>
## 🇺🇸 English

A collection of professional Python tools for cybersecurity automation, covering network analysis, digital forensics, and web auditing.

### 🛠️ Included Labs

* **Advanced Network Scanner:** Hybrid port scanning (ranges/lists) with real-time service detection.
* **File Integrity Manager:** SHA-256 hashing system with JSON database for automated file tampering detection (Mini-IDS).
* **Web Security Auditor:** HTTP header analysis tool with banner grabbing and risk scoring system.

---

### 🚀 Instalación / Installation

```bash
# Clonar el repositorio
git clone [https://github.com/CPineyrua/Python_Security_Labs.git](https://github.com/CPineyrua/Python_Security_Labs.git)

# Instalar dependencias
pip install requests