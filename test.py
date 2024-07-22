import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import TwoSlopeNorm
from matplotlib.cm import ScalarMappable, get_cmap
import pandas as pd

# Assuming Dir1 is a DataFrame with 'FPKM' and 'Gene' columns
Dir1 = pd.DataFrame({
    "FPKM": [5, 10, 20, 40, 60, 80, 100, 120],
    "Gene": range(1, 9)
})

# Create a bidirectional color scale
norm = TwoSlopeNorm(vmin=Dir1['FPKM'].min(), vcenter=Dir1['FPKM'].median(), vmax=Dir1['FPKM'].max())
cmap = get_cmap('RdBu_r')

# Plot 1: Scatter plot with segments
fig, ax = plt.subplots(figsize=(10, 6))

# Corrected to use 'ax' directly since we have only one subplot
ax.set_xlabel("FPKM")
ax.set_ylabel("Gene")
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.axhline(0, color='grey', linewidth=1)  # Use axhline since Gene is on the y-axis

# Loop to plot segments and scatter points with FPKM on the x-axis and Gene on the y-axis
for _, row in Dir1.iterrows():
    ax.plot([0, row['FPKM']], [row['Gene'], row['Gene']], color='grey', alpha=0.8, linewidth=1.2)
    ax.scatter(row['FPKM'], row['Gene'], c=[cmap(norm(row['FPKM']))], s=100, edgecolor='black')

ax.set_title('Lightest color means nothing\n(neither mean nor median).')

# Plot 2: Colorbar
# Adjust subplot for the colorbar
fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, cax=cbar_ax, orientation='vertical')

plt.show()