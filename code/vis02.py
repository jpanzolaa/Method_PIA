import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Usar un estilo gráfico profesional
plt.style.use('seaborn-v0_8-darkgrid')

# Load the CSV files into dataframes
file_1 = 'Mod_1_DF.csv'
file_4 = 'Mod_4_DF.csv'

# Load the CSV files into dataframes
matriz1 = pd.read_csv(file_1, index_col=0)
matriz4 = pd.read_csv(file_4, index_col=0)

# Calculate individual min and max values for each matrix
min_value_matriz1 = matriz1.min().min()
max_value_matriz1 = matriz1.max().max()

min_value_matriz4 = matriz4.min().min()
max_value_matriz4 = matriz4.max().max()

# Create a mask for missing values (NaN)
mask1 = matriz1.isnull()
mask4 = matriz4.isnull()

# Labels for the rows and columns
empresas = matriz1.index  # Companies (Y-axis)
anos = matriz1.columns    # Years (X-axis)

# Create a figure with 2 subplots (one for each matrix)
fig, axs = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [1, 1]})

# Set color map to "coolwarm"
cmap = 'coolwarm'

# Plot heatmap for Matriz 1 with professional touches and mask for NaN values
sns.heatmap(matriz1, cmap=cmap, annot=True, fmt=".1f", cbar=False, ax=axs[0], vmin=min_value_matriz1, vmax=max_value_matriz1,
            annot_kws={"size": 10, "weight": 'bold'}, linewidths=0.1, linecolor='black', mask=mask1)

axs[0].set_title('(a)', fontsize=16, weight='bold')
axs[0].set_yticklabels(empresas, fontsize=12, weight='bold')
axs[0].set_xticklabels(anos, rotation=45, ha='right', fontsize=12, weight='bold')
axs[0].set_ylabel('Brand', fontsize=14, weight='bold')
axs[0].set_xlabel('Year', fontsize=14, weight='bold')

# Plot heatmap for Matriz 4 with professional touches and mask for NaN values
sns.heatmap(matriz4, cmap=cmap, annot=True, fmt=".1f", cbar=False, ax=axs[1], vmin=min_value_matriz4, vmax=max_value_matriz4,
            annot_kws={"size": 10, "weight": 'bold'}, linewidths=0.1, linecolor='black', mask=mask4)

axs[1].set_title('(b)', fontsize=16, weight='bold')
axs[1].set_xticklabels(anos, rotation=45, ha='right', fontsize=12, weight='bold')
axs[1].set_yticks([])  # Hide Y-axis labels for the second plot
axs[1].set_xlabel('Year', fontsize=14, weight='bold')
axs[1].set_ylabel(' ', fontsize=14, weight='bold')

# Adjust colorbars to be uniform and professional
cbar_ax = fig.add_axes([0.93, 0.15, 0.02, 0.7])  # Place for a global colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(min_value_matriz1, min_value_matriz4), 
                                                         vmax=max(max_value_matriz1, max_value_matriz4)))
sm.set_array([])
fig.colorbar(sm, cax=cbar_ax, label='Scale', orientation='vertical')

# Adjust layout to minimize whitespace and improve presentation
plt.tight_layout(rect=[0, 0, 0.92, 1])  # Adjust layout for space for colorbar

# Save the figure in high resolution for publication
plt.savefig('figures/Ana01.png', bbox_inches='tight', dpi=300)
plt.savefig('figures/Ana01.pdf', bbox_inches='tight', dpi=300)

# Display the plot
plt.show()






'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV files into dataframes
file_1 = 'Mod_1_DF.csv'
file_4 = 'Mod_4_DF.csv'

# Load the CSV files into dataframes
matriz1 = pd.read_csv(file_1, index_col=0)
matriz4 = pd.read_csv(file_4, index_col=0)

# Calculate individual min and max values for each matrix
min_value_matriz1 = matriz1.min().min()
max_value_matriz1 = matriz1.max().max()

min_value_matriz4 = matriz4.min().min()
max_value_matriz4 = matriz4.max().max()

# Labels for the rows and columns
empresas = matriz1.index  # Companies (Y-axis)
anos = matriz1.columns    # Years (X-axis)

# Create a figure with 2 subplots (one for each matrix)
fig, axs = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [1, 1]})

# Set color map
cmap = 'coolwarm'

# Plot heatmap for Matriz 1
heatmap1 = axs[0].imshow(matriz1, cmap=cmap, vmin=min_value_matriz1, vmax=max_value_matriz1, aspect='auto')
axs[0].set_title('(a)', fontsize=14, weight='bold')
axs[0].set_yticks(np.arange(len(empresas)))
axs[0].set_yticklabels(empresas, fontsize=12)
axs[0].set_xticks(np.arange(len(anos)))
axs[0].set_xticklabels(anos, rotation=45, ha='right', fontsize=12)
axs[0].grid(False)
axs[0].set_ylabel('Brand', fontsize=12)
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)
axs[0].spines['left'].set_visible(True)
axs[0].spines['bottom'].set_visible(True)
fig.colorbar(heatmap1, ax=axs[0], fraction=0.046, pad=0.04).set_label('Scale', fontsize=12)

# Plot heatmap for Matriz 4
heatmap4 = axs[1].imshow(matriz4, cmap=cmap, vmin=min_value_matriz4, vmax=max_value_matriz4, aspect='auto')
axs[1].set_title('(b)', fontsize=14, weight='bold')
axs[1].set_xticks(np.arange(len(anos)))
axs[1].set_xticklabels(anos, rotation=45, ha='right', fontsize=12)
axs[1].set_yticks([])  # Hide Y-axis labels for the second plot
axs[1].grid(False)
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)
axs[1].spines['left'].set_visible(True)
axs[1].spines['bottom'].set_visible(True)
fig.colorbar(heatmap4, ax=axs[1], fraction=0.046, pad=0.04).set_label('Scale', fontsize=12)

# Adjust the layout to minimize whitespace
plt.tight_layout()

# Save the figure in high resolution for publication
plt.savefig('figures/Ana01.png', bbox_inches='tight', dpi=300)
plt.savefig('figures/Ana01.pdf', bbox_inches='tight', dpi=300)

# Display the plot
plt.show()

'''