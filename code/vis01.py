import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV files into dataframes
file_1 = 'Mod_1_DF.csv'
file_4 = 'Mod_4_DF.csv'

# Load the CSV files into dataframes
matriz1 = pd.read_csv(file_1, index_col=0)
matriz4 = pd.read_csv(file_4, index_col=0)

# Prepare a list of the matrices to iterate over (only Matriz 1 and Matriz 4)
matrices = [matriz1, matriz4]

# Create a figure with 2 subplots for each matrix's horizontal stacked bar chart
fig, axs = plt.subplots(1, 2, figsize=(28, 8), sharey=True)

# List of subplot labels
subplot_labels = ['(a)', '(b)']

# Loop through matrices and generate a horizontal stacked bar plot for each
for i, (matriz, ax) in enumerate(zip(matrices, axs), start=0):
    # Plot horizontal stacked bar chart for each matrix
    matriz.plot(kind='barh', stacked=True, ax=ax, color=sns.color_palette("Paired", len(matriz.columns)))

    # Set titles and labels
    ax.set_title(f'{subplot_labels[i]}', fontsize=14, weight='bold')
    ax.set_xlabel('Value', fontsize=12)
    ax.set_ylabel('Brand', fontsize=12)

    # Customize appearance
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# Adjust layout to minimize whitespace
plt.tight_layout()

# Guardar la figura en alta resolución para publicación
plt.savefig('figures\Ana02.png', bbox_inches='tight', dpi=300)
plt.savefig('figures\Ana02.pdf', bbox_inches='tight', dpi=300)

# Display the plot
plt.show()
