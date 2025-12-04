# Análisis de temperatura en México (1902–2011)

## 1. Introducción

El objetivo de este proyecto es analizar el comportamiento de la temperatura en México entre 1902 y 2011 utilizando datos agregados por regiones. Se busca identificar zonas con mayor calentamiento relativo y explorar posibles implicaciones para la planeación urbana, agrícola e infraestructura.

Las preguntas específicas son:

1. ¿Qué regiones de México muestran mayores incrementos en temperatura media a lo largo del periodo 1902–2011?
2. ¿En qué zonas se concentran las temperaturas máximas extremas y cómo se relacionan con la temperatura media?
3. ¿Existen regiones donde la brecha entre temperatura mínima y máxima promedio sea especialmente alta (amplitud térmica)?
4. ¿Cómo puede utilizarse este análisis para apoyar decisiones (infraestructura, salud pública, agricultura, energía)?

## 2. Datos y metodología

- **Fuente de datos:** dataset sintético `temperaturas_mx_1902_2011.csv`, generado a partir de un modelo simplificado que simula:
  - Temperatura mínima (tmin_c)
  - Temperatura máxima (tmax_c)
  - Temperatura media (tmean_c)
  - Índice de extremos (extreme_index)
  - Para 5 regiones: Noroeste, Noreste, Centro, Occidente y Sureste.
- **Cobertura temporal:** 1902–2011 con cortes cada 5 años.
- **Variables claves:**
  - `region_id`, `region_name`
  - `lat`, `lon`
  - `year`
  - `tmin_c`, `tmax_c`, `tmean_c`, `extreme_index`

El análisis se implementa en Python mediante el script `src/visualization/basic_analysis.py`, que:
- Carga el dataset procesado.
- Calcula estadísticas descriptivas por región y año.
- Genera gráficos de tendencias de temperatura y amplitud térmica.

## 3. Resultados principales (ejemplo de redacción)

### 3.1 Tendencias de temperatura media

En todas las regiones analizadas se observa una **tendencia positiva** en la temperatura media a lo largo del periodo 1902–2011.  
El incremento es consistente con un calentamiento gradual, con variaciones entre regiones:

- Algunas regiones (por ejemplo, Centro u Occidente) muestran una pendiente ligeramente más pronunciada.
- Las figuras de tendencia temporal ilustran cómo la temperatura media aumenta de manera casi lineal, con pequeñas fluctuaciones interanuales.

### 3.2 Temperaturas máximas y extremos

Las temperaturas máximas (`tmax_c`) siguen un patrón similar al de la temperatura media, con valores más elevados en las regiones [ajustar según los gráficos que veas].  

El **índice de extremos** (`extreme_index`) permite identificar:
- Años y regiones donde las temperaturas máximas se alejan más de un valor de referencia (por ejemplo, 30 °C).
- Potenciales periodos de mayor estrés térmico que podrían asociarse a riesgos para salud, agricultura o demanda de energía.

### 3.3 Amplitud térmica (tmax – tmin)

La amplitud térmica tiende a ser mayor en regiones [ajustar según los resultados], lo que indica:

- Mayor contraste entre las temperaturas diurnas y nocturnas.
- Posibles implicaciones para confort térmico, demanda energética y ciertos cultivos.

## 4. Discusión y posibles aplicaciones

Los resultados, aunque basados en un dataset sintético, ilustran cómo un análisis estructurado de temperatura por regiones y en una serie histórica larga puede:

- Ayudar a **priorizar estudios de vulnerabilidad climática** en regiones con mayor calentamiento relativo.
- Orientar la **planeación de infraestructura** (por ejemplo, diseño de sistemas de climatización, materiales resistentes al calor).
- Apoyar decisiones en **agricultura**, como la selección de cultivos o la planificación de riego.
- Servir como base para integrar **indicadores de riesgo en salud pública** relacionados con olas de calor.

## 5. Conclusiones

- Se observa una tendencia general al **incremento de la temperatura media** en todas las regiones consideradas.
- La combinación de temperatura media, máxima, mínima y un índice de extremos permite tener una visión más completa del comportamiento térmico.
- Este tipo de análisis puede integrarse en sistemas de apoyo a la decisión para sectores como infraestructura, salud, energía y agricultura.

## 6. Trabajo futuro

- Sustituir el dataset sintético por datos observados reales.
- Aumentar la resolución espacial (municipios, cuadrículas).
- Incorporar otras variables climáticas (precipitación, humedad, etc.).
- Desarrollar dashboards interactivos (ver Tema 2 del proyecto) para facilitar la exploración de los datos.
