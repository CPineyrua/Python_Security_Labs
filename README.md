# Python Security Labs 🛡️

[Español](#español) | [English](#english)

---

<a name="español"></a>
## 🇪🇸 Español

### Descripción
Este repositorio contiene una colección de herramientas experimentales desarrolladas en Python para el análisis de redes y auditoría de seguridad.

#### Laboratorio 01: Escáner de Puertos TCP Básico
Este script realiza un escaneo de puertos específico (80, 443) sobre una dirección IP. Utiliza el protocolo de enlace de tres vías (**TCP Three-Way Handshake**) para determinar la disponibilidad del servicio.

**Conceptos Técnicos Aplicados:**
* **Librería Socket:** Comunicación de bajo nivel.
* **Manejo de Excepciones:** Robustez mediante bloques `try-except-finally`.
* **F-Strings:** Reportes dinámicos y legibles.

---

<a name="english"></a>
## 🇺🇸 English

### Description
This repository features a collection of experimental Python tools designed for network analysis and security auditing.

#### Lab 01: Basic TCP Port Scanner
This script performs a targeted port scan (80, 443) on a given IP address. It leverages the **TCP Three-Way Handshake** protocol to determine service availability.

**Technical Concepts Applied:**
* **Socket Library:** Low-level network communication.
* **Exception Handling:** Robustness via `try-except-finally` blocks.
* **F-Strings:** Dynamic and readable reporting.

---

### 🚀 Usage / Uso
```bash
python escaneo.py