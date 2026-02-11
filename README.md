# Python Security Labs 🛡️

[Español](#español) | [English](#english)

<a name="español"></a>
## 🇪🇸 Español

Este repositorio es un ecosistema de herramientas profesionales desarrolladas en Python para la automatización de tareas de ciberseguridad, abarcando desde el análisis de redes hasta la forense digital y auditoría web.

### 🛠️ Laboratorios Disponibles

#### 1. Network Scanner (v5 - Professional CLI)
Escáner de puertos avanzado que identifica servicios activos mediante TCP.
* **Capacidades:** Soporta escaneo por rangos (`20-80`) y listas específicas (`22,80,443`).
* **Uso:** `python network_scanner_v5.py 127.0.0.1 20-443`

#### 2. Integrity Manager (IDS Simulado)
Sistema de detección de integridad basado en criptografía (SHA-256).
* **Capacidades:** Registro de huellas digitales y verificación automática con base de datos JSON.
* **Uso:** `python file_integrity.py register archivo.txt` o `verify archivo.txt`

#### 3. Web Security Auditor
Scanner de vulnerabilidades en cabeceras HTTP y detección de servidor.
* **Capacidades:** Banner Grabbing y sistema de puntuación de riesgo (Scoring 0/4).
* **Uso:** `python web_security_scanner.py google.com`

---

<a name="english"></a>
## 🇺🇸 English

This repository is a collection of professional Python tools designed for cybersecurity automation, ranging from network analysis to digital forensics and web auditing.

### 🛠️ Included Labs

#### 1. Network Scanner (v5 - Professional CLI)
Advanced port scanner using TCP protocol to identify active services.
* **Key Features:** Supports range scanning (`20-80`) and specific port lists (`22,80,443`).
* **Usage:** `python network_scanner_v5.py 127.0.0.1 20-443`

#### 2. Integrity Manager (Simulated IDS)
Cryptography-based integrity detection system to protect files against tampering.
* **Key Features:** SHA-256 fingerprinting and automated verification with JSON persistence.
* **Usage:** `python file_integrity.py register file.txt` or `verify file.txt`

#### 3. Web Security Auditor
HTTP header vulnerability scanner and server banner grabbing tool.
* **Key Features:** Risk scoring system (0/4) and security header analysis (CSP, HSTS, XFO).
* **Usage:** `python web_security_scanner.py google.com`

---

### 🚀 Setup / Instalación

```bash
# Clone the repository
git clone [https://github.com/CPineyrua/Python_Security_Labs.git](https://github.com/CPineyrua/Python_Security_Labs.git)

# Install dependencies
pip install requests