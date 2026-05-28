# Trabajo Práctico: Gestión Colaborativa, Control de Versiones y Organización Empresarial (Git, GitHub y Jira)

## Datos del Proyecto
* **Institución:** Universidad Tecnológica Nacional (UTN)
* **Carrera:** Tecnicatura Universitaria en Programación (Modalidad a Distancia)
* **Cátedra:** Organización Empresarial
* **Año Lectivo:** 2026

## Célula de Desarrollo (Simulada)
* **P1 - Líder y Organizador (Rol: Hugo):** Responsable de la inicialización de la estructura del repositorio y gobernanza.
* **P2 - Desarrollador Técnico (Rol: Paco):** Responsable de la lógica algorítmica y procesamiento de datos.
* **P3 - Revisor y QA (Rol: Luis):** Responsable de la documentación, revisión por pares (Peer Review) y aseguramiento de la calidad.

## Escenario Seleccionado: Escenario B – Análisis de Ventas de una Pequeña Empresa
Este proyecto analiza un conjunto de datos comerciales simulados para extraer métricas clave de rendimiento empresarial y generar visualizaciones que faciliten la toma de decisiones estratégicas.

### Indicadores Calculados:
1. **Ventas Totales (Ingresos):** Sumatoria total de las transacciones (precio * cantidad_vendida).
2. **Producto más vendido:** Identificación del artículo con mayor volumen de unidades colocadas.
3. **Evolución de ventas por mes:** Tendencia comercial a lo largo del primer semestre.

---

## Estructura del Repositorio
El proyecto mantiene una separación de responsabilidades bajo la siguiente estructura de carpetas:

```text
repo-proyecto/
├── datos/
│   └── ventas.csv              # Dataset comercial de entrada
├── scripts/
│   └── analisis_ventas.py      # Código fuente de procesamiento en Python
├── resultados/
│   └── evolucion_ventas.png    # Gráfica exportada de evolución de ventas
├── .gitignore                  # Exclusión de archivos temporales
└── README.md                   # Documentación general del proyecto
