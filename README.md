Framework de Automatización E-Commerce (SauceDemo)

Este proyecto es un framework de pruebas automatizadas profesional utilizando el patrón de diseño **Page Object Model (POM)**.

##  Tecnologías utilizadas
* **Lenguaje:** Python 3.x
* **Herramientas de Testing:** PyTest
* **Automatización Web:** Selenium WebDriver
* **Reportes:** PyTest-HTML
* **Infraestructura:** AWS (EC2, S3) e IAM para seguridad.
* **CI/CD:** GitHub Actions

##  Instalación
1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`.
3. Activar entorno virtual: `.\venv\Scripts\activate` (Windows).
4. Instalar dependencias: `pip install -r requirements.txt`.

##  Ejecución de Pruebas
Para ejecutar todos los tests y generar un reporte:
```bash
pytest --html=report.html