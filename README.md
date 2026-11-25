# CyberSec-MasterUOC-Portfolio

Selección de laboratorios prácticos, arquitectura de red y bastionado de sistemas del **Máster en Ciberseguridad y Privacidad (UOC)**, especialidad de Sistemas.

> No es un volcado de todas las prácticas del máster: solo incluyo las más representativas. El repositorio se va ampliando a medida que avanzo.

## Prácticas destacadas

| Práctica | Qué demuestra | Herramientas |
|---|---|---|
| [**Fundamentos de Ciberseguridad · PR3 Ataques**](./Fundamentos%20de%20Ciberseguridad/PR3-Ataques) | Auditoría completa de una red hostil emulada: reconocimiento, crackeo WPA2, fuerza bruta SSH y SMB, LFI, escalada de privilegios, web shell con RCE y pivoting mediante túnel SOCKS hacia una red interna. 20 tareas documentadas con evidencias. | Kathará, Docker, Kali Linux, Nmap, fping, Aircrack-ng, Hydra, John the Ripper, Gobuster, ffuf, Metasploit, smbclient, proxychains4 |
| [**Seguridad y Pentesting de Servidores de Datos · PEC 1**](./Seguridad%20y%20Pentesting%20de%20Servidores%20de%20Datos/PEC1_Bastionado_DB) | Bastionado de MariaDB y MongoDB sobre Ubuntu Server: TLS, RBAC, cifrado en reposo y a nivel de columna, auditoría, restricción por IP, copias de seguridad cifradas. Incluye el diseño de la arquitectura segura de una plataforma de telemedicina (RGPD). | MariaDB, MongoDB, OpenSSL, GPG |
| [**Seguridad y Pentesting de Servidores de Datos · PRAC 1 Ataques**](./Seguridad%20y%20Pentesting%20de%20Servidores%20de%20Datos/PRAC1_Ataques_Servidores_Datos) | Ataques a servidores de datos sobre un entorno Docker: inyección SQL manual (booleana, errores, `UNION`, extracción de esquemas y usuarios) y automatizada, bypass de un formulario de login con filtros y lectura de ficheros mediante path traversal. | SQLmap, MariaDB, Docker, navegador y peticiones HTTP manuales |
| [**IA aplicada a la Ciberseguridad · PR1 Limpieza de datos**](./IA%20aplicada%20a%20la%20Ciberseguridad/PR1_Limpieza_Datos) | Limpieza y análisis exploratorio de 11.775 eventos de tráfico web y diseño de reglas heurísticas para detectar fuerza bruta, escaneo de vulnerabilidades, inyecciones y micro-DDoS. | Python, pandas, NumPy, matplotlib, seaborn, Jupyter |
| [**IA aplicada a la Ciberseguridad · PR2 Detección de intrusiones**](./IA%20aplicada%20a%20la%20Ciberseguridad/PR2_Deteccion_Intrusiones) | Detector de intrusiones binario con Random Forest sobre 8.000 flujos de red sintéticos (tráfico normal y cuatro familias de ataque): preprocesado con pipeline, división estratificada, búsqueda de 72 combinaciones de hiperparámetros con validación cruzada e importancia de variables por permutación. | Python, scikit-learn, pandas, matplotlib, Jupyter |
| [**Privacidad · PR1 Publicación de datos**](./Privacidad/PR1_Publicacion_Datos) | Análisis del riesgo de reidentificación al publicar datos de un hospital y anonimización de un conjunto de datos con jerarquías de generalización, k-anonimato y otros modelos de privacidad, buscando el equilibrio entre privacidad y pérdida de información. | ARX Data Anonymization Tool |

## Herramientas y tecnologías

- **Pentesting y redes**: SQLmap, Nmap, Metasploit, Hydra, John the Ripper, Aircrack-ng, Gobuster, ffuf, proxychains4, túneles SSH
- **Bastionado y bases de datos**: MariaDB, MongoDB, OpenSSL, GPG
- **Entornos de laboratorio**: Kathará, Docker, Kali Linux, Ubuntu Server
- **Análisis de datos**: Python, pandas, NumPy, scikit-learn, matplotlib, seaborn, Jupyter Notebook
- **Privacidad y anonimización**: ARX Data Anonymization Tool

## Aviso

Todas las pruebas se han realizado en entornos de laboratorio controlados, con fines exclusivamente académicos.

## Autor

**Alejandro Torres** · [GitHub](https://github.com/aletorres642)
