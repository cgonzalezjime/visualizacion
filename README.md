
# Visualización Interactiva de Empleos en el Área de Datos

Este proyecto ofrece un dashboard interactivo desarrollado con **Streamlit** y **Plotly**, que permite explorar el mercado laboral en el ámbito de los datos. A través de diversos filtros y gráficos, podrás descubrir patrones salariales, tipos de contrato y tendencias por nivel de experiencia.

**App en línea**:  
[Abrir aplicación en Streamlit Cloud](https://visualizacion-kk78sqdt9ppxxsaavjzrra.streamlit.app)

---

## Funcionalidades principales

- Filtrado por **año**, **nivel de experiencia** y **modalidad de trabajo**.
- Visualización del **salario promedio por categoría profesional**.
- Gráfico **treemap** y **sunburst** jerárquico por puesto, categoría y tipo de contrato.
- Mapa de burbujas por país y categoría.
- Distribución salarial (boxplot) por nivel de experiencia.
- Gráfico **animado** de evolución salarial por año y categoría.

---

## Estructura de archivos

| Archivo | Descripción |
|--------|-------------|
| `streamlit_app_final.py` | Script principal con el dashboard interactivo. |
| `jobs_in_data.csv`       | Conjunto de datos con información de empleos en ciencia de datos. |
| `requirements.txt`       | Dependencias necesarias para ejecutar la app en Streamlit Cloud o localmente. |

---

## Cómo ejecutar localmente

1. Clona este repositorio:
   ```bash
   git clone https://github.com/cgonzalezjime/visualizacion.git
   cd visualizacion
   ```

2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la app:
   ```bash
   streamlit run streamlit_app_final.py
   ```

---

## Requisitos

- Python 3.8 o superior
- Paquetes: `streamlit`, `pandas`, `plotly`

---

## Autor

**Carlos González Jiménez**  
Proyecto académico para la UOC - Grado en Ciencia de Datos.
