import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los archivos CSV seleccionados
mod_1_df = pd.read_csv('mnt\data\Mod_1_DF.csv')
mod_4_df = pd.read_csv('mnt\data\Mod_4_DF.csv')

# Filtrar las columnas relevantes
datos_modificados_ve = pd.read_excel('mnt\data\Datos_Modificados VE(SYD).xlsx')
datos_modificados_ve = datos_modificados_ve[['Empresa', 'Model', 'Current Price', 'Initial Price']]

# Reorganizar los DataFrames seleccionados
mod_1_melted = mod_1_df.melt(id_vars=['Empresa'], var_name='Model', value_name='Estimated Price Mod 1').dropna()
mod_4_melted = mod_4_df.melt(id_vars=['Empresa'], var_name='Model', value_name='Estimated Price Mod 4').dropna()

# Convertir los años del modelo a enteros
mod_1_melted['Model'] = mod_1_melted['Model'].astype(int)
mod_4_melted['Model'] = mod_4_melted['Model'].astype(int)

# Unir los datos reales con los resultados estimados de los dos métodos
merged_data = datos_modificados_ve.merge(mod_1_melted, on=['Empresa', 'Model'], how='left') \
                                 .merge(mod_4_melted, on=['Empresa', 'Model'], how='left')

# Calcular los errores absolutos para los dos métodos
merged_data['Error Mod 1'] = abs(merged_data['Current Price'] - merged_data['Estimated Price Mod 1'])
merged_data['Error Mod 4'] = abs(merged_data['Current Price'] - merged_data['Estimated Price Mod 4'])

# Crear un gráfico de densidades con el punto de interés agregado
plt.figure(figsize=(10, 6))

# Colores profesionales para cada curva
colors = ['#1f77b4', '#d62728']

# Actualizamos las leyendas con los nombres de los métodos correspondientes
for column, label, color in zip(['Error Mod 1', 'Error Mod 4'],
                                ['Straight-Line Method (SLM)', 'Adverse Selection Method'],
                                colors):
    # Limpiar los NaN e infinitos antes de graficar
    valid_data = merged_data[['Model', column]].dropna().replace([np.inf, -np.inf], np.nan).dropna()
    valid_data.groupby('Model')[column].mean().plot(kind='density', ax=plt.gca(), label=label, alpha=0.8, color=color)

# Coordenadas del punto de interés para el método de Selección Adversa
x_intersection = 1.8668e+08
y_intersection = 5.582e-09

# Añadir el punto de intersección a la gráfica sin la etiqueta de texto
plt.scatter(x_intersection, y_intersection, color='red', label="Intersection Point", zorder=5)

# Configurar el gráfico con títulos en inglés y colores profesionales
plt.title("Density of Price Estimations by Vehicle Model Year", fontsize=14)
plt.xlabel("Vehicle Model Year")
plt.ylabel("Density of Price Estimation")
plt.legend()
plt.grid(True)

# Save the figure in high resolution for publication
plt.savefig('figures/Ana03.png', bbox_inches='tight', dpi=300)
plt.savefig('figures/Ana03.pdf', bbox_inches='tight', dpi=300)

# Mostrar el gráfico
plt.show()
