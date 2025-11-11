# ProyectoOptica

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Estado-En%20desarrollo-yellow.svg)](#)
[![Pull Requests](https://img.shields.io/badge/Contribuciones-Bienvenidas-success.svg)](https://github.com/WetZap/ProyectoOptica/pulls)
[![Made with ❤️ by WetZap](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](https://github.com/WetZap)

---

## 🧠 Descripción
**ProyectoOptica** es una herramienta educativa desarrollada en **Python** para la resolución y verificación de problemas de **Óptica**.  
Incluye recursos de referencia, gráficos ilustrativos y cálculos automáticos para estudiantes y docentes de física.

El objetivo del proyecto es ofrecer una base adaptable, sencilla y útil para analizar ejercicios típicos de óptica geométrica o física.

---

## ✨ Características principales
- 📜 Script principal en Python (`Optica.py`) con los cálculos fundamentales.  
- 📊 Archivo de datos (`Metales_IndRef.xlsx`) con propiedades e índices de refracción de metales.  
- 🧩 Diagrama vectorial (`Optica.svg`) para representaciones visuales.  
- 🧮 Estructura modular, fácil de adaptar y expandir.  

---

## ⚙️ Requisitos
- Python **3.8 o superior**  
- Bibliotecas recomendadas: `numpy`, `pandas`, `matplotlib`  

```bash
python -m venv venv
source venv/bin/activate     # Linux / macOS
venv\Scripts\activate        # Windows
pip install numpy pandas matplotlib
```
---

## 🚀 Instalación rápida
```bash
1. Clona el repositorio:  
# git clone https://github.com/WetZap/ProyectoOptica.git
2. Entra al directorio:  
# cd ProyectoOptica
3. (Opcional) Crea un entorno virtual e instala las dependencias.  
4. Ejecuta el script principal:  
# python Optica.py
```
> 💡 *Los comandos están comentados para evitar errores al copiar. Descoméntalos en tu terminal según corresponda.*

---

## 🧰 Uso básico
1. Abre el proyecto o ejecuta directamente `Optica.py`.  
2. Introduce los datos requeridos (índices, ángulos, longitudes, etc.).  
3. Analiza la salida por consola o en los archivos de resultados generados.  
4. Usa el archivo `Metales_IndRef.xlsx` como referencia de índices ópticos.  

---

## 🤝 Cómo contribuir
1. Haz un **fork** del proyecto.  
2. Crea una rama con tu mejora: `feature/nueva-funcionalidad`.  
3. Realiza tus cambios y añade comentarios claros.  
4. Envía un **Pull Request** con la descripción detallada de los cambios.

[![GitHub forks](https://img.shields.io/github/forks/WetZap/ProyectoOptica?style=social)](https://github.com/WetZap/ProyectoOptica/fork)
[![GitHub stars](https://img.shields.io/github/stars/WetZap/ProyectoOptica?style=social)](https://github.com/WetZap/ProyectoOptica/stargazers)

---

## 🧩 Buenas prácticas y sugerencias
- Incluir un archivo `requirements.txt` con dependencias exactas.  
- Documentar funciones y ejemplos en el código.  
- Añadir pequeños *tests* para verificar la corrección de cálculos.  
- Exportar resultados a formatos como `.csv` o `.json`.

---

## 📜 Licencia
Este proyecto está distribuido bajo la **Licencia MIT**.  
Consulta el archivo [`LICENSE`](LICENSE) para más información.

---

## 👨‍🔬 Créditos
**Autor:** [WetZap](https://github.com/WetZap)  
Proyecto académico y educativo desarrollado con fines de aprendizaje.

---

## 🧭 Roadmap
- [ ] Añadir ejemplos resueltos paso a paso  
- [ ] Implementar interfaz CLI con ayuda (`--help`)  
- [ ] Incorporar visualización de resultados  
- [ ] Añadir tests unitarios  

---


