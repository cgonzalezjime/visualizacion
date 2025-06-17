
import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv("jobs_in_data.csv")

df = load_data()

# Título y descripción inicial
st.title("Visualización Interactiva de Empleos en el Área de Datos")
st.markdown("""
Explora el mercado laboral en el campo de los datos mediante visualizaciones interactivas. 
Este dashboard permite analizar salarios, categorías profesionales, tipos de contrato y distribución geográfica.

Los gráficos que verás aquí están diseñados para ayudarte a descubrir patrones y responder preguntas como:
- ¿Qué categorías tienen los salarios más altos?
- ¿Cómo varía el salario según la experiencia o el país?
- ¿Qué modalidades de trabajo predominan en el sector?

Utiliza los filtros del panel lateral para adaptar el análisis a tus intereses.
""")

# Sidebar: filtros
st.sidebar.header("Filtros Interactivos")
year = st.sidebar.selectbox("Selecciona el año", sorted(df["work_year"].unique()), index=0)
experience = st.sidebar.multiselect("Nivel de experiencia", df["experience_level"].unique(), default=df["experience_level"].unique())
setting = st.sidebar.multiselect("Modalidad de trabajo", df["work_setting"].unique(), default=df["work_setting"].unique())

filtered_df = df[
    (df["work_year"] == year) &
    (df["experience_level"].isin(experience)) &
    (df["work_setting"].isin(setting))
]

# Gráfico de barras
st.subheader("Salario Promedio por Categoría Profesional")
st.markdown("Este gráfico de barras horizontales muestra qué categorías tienen los salarios promedio más altos.")
fig1 = px.bar(
    filtered_df.groupby("job_category")["salary_in_usd"].mean().sort_values().reset_index(),
    x="salary_in_usd", y="job_category", orientation="h",
    labels={"salary_in_usd": "Salario Promedio (USD)", "job_category": "Categoría"}
)
st.plotly_chart(fig1, use_container_width=True)

# Treemap
st.subheader("Treemap: Salario por Categoría y Puesto")
st.markdown("El tamaño del bloque representa el salario total para cada puesto dentro de su categoría. Ideal para detectar jerarquías.")
fig2 = px.treemap(
    filtered_df,
    path=["job_category", "job_title"],
    values="salary_in_usd",
    color="salary_in_usd",
    color_continuous_scale="RdBu",
    title="Salario por Categoría y Puesto"
)
st.plotly_chart(fig2, use_container_width=True)

# Sunburst Chart
st.subheader("Distribución Jerárquica de Salarios (Sunburst Chart)")
st.markdown("""
Este gráfico jerárquico representa tres niveles:
- **Centro**: Categoría profesional.
- **Segundo anillo**: Nivel de experiencia.
- **Tercer anillo**: Tipo de contrato.

El tamaño y el color indican el salario acumulado para cada combinación.
""")

fig3 = px.sunburst(
    filtered_df,
    path=["job_category", "experience_level", "employment_type"],
    values="salary_in_usd",
    color="salary_in_usd",
    color_continuous_scale="Tealgrn"
)
st.plotly_chart(fig3, use_container_width=True)

# Mapa burbuja
st.subheader("Mapa de Burbujas: Salario por País y Categoría")
st.markdown("Cada burbuja representa un país. Su tamaño depende del salario total y el color indica la categoría profesional.")
fig4 = px.scatter_geo(
    filtered_df,
    locations="employee_residence",
    locationmode="country names",
    size="salary_in_usd",
    color="job_category",
    hover_name="employee_residence"
)
st.plotly_chart(fig4, use_container_width=True)

# Boxplot
st.subheader("Distribución Salarial por Nivel de Experiencia")
st.markdown("El boxplot muestra cómo varía el salario dentro de cada nivel de experiencia, destacando valores mínimos, máximos y medianas.")
fig5 = px.box(
    filtered_df, x="experience_level", y="salary_in_usd", color="experience_level",
    labels={"salary_in_usd": "Salario (USD)", "experience_level": "Experiencia"}
)
st.plotly_chart(fig5, use_container_width=True)

# Gráfico animado
st.subheader("Evolución Salarial por Año y Categoría")
st.markdown("Este gráfico animado permite observar cómo han evolucionado los salarios en distintas categorías y niveles de experiencia a lo largo del tiempo.")
fig6 = px.scatter(
    df,
    x="experience_level", y="salary_in_usd",
    animation_frame="work_year",
    color="job_category",
    size="salary_in_usd",
    hover_name="job_title"
)
st.plotly_chart(fig6, use_container_width=True)

# Conclusión
st.markdown("""
### Conclusión
Gracias a estas visualizaciones interactivas, puedes identificar:
- Qué perfiles tienen mejores salarios.
- Cómo influye la experiencia y la modalidad laboral.
- Qué países ofrecen mejores oportunidades en el campo de los datos.

Explora, filtra y analiza para sacar tus propias conclusiones.
""")
