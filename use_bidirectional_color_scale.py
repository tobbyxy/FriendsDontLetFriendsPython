# Import necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import TwoSlopeNorm
from matplotlib import cm
from matplotlib.cm import ScalarMappable

# Simulate data
# Just some arbitrary sequential/directional data
Dir1 = pd.DataFrame({
    "FPKM": [5, 10, 20, 40, 60, 80, 100, 120],
    "Gene": range(1, 9)
})

Dir2 = pd.DataFrame({
    "log2FC": [-10, -4, -2, 0, 2, 4, 10],
    "Gene": range(1, 8)
})

Dir3 = pd.DataFrame({
    "z.score": [-2.5, -2, -1, 0, 1, 2, 2.5],
    "Gene": range(1, 8)
})

# Display the first few rows of Dir3
print(Dir3.head())



# Good example 1
fig, ax = plt.subplots(1, 2, gridspec_kw={'width_ratios': [10, 1]}, figsize=(6, 10))

# Plot A
sns.scatterplot(data=Dir1, y="Gene", x="FPKM", size="FPKM", hue="FPKM", palette="viridis", sizes=(100, 400), ax=ax[0])
#ax[0].invert_xaxis()  # For coord_flip effect
ax[0].set_title("Darkest color = Min\nLightest color = Max")
ax[0].set_ylabel("Gene")
ax[0].set_xlabel("FPKM")
ax[0].grid(True, which='both', linestyle='--', linewidth=0.5)
ax[0].axhline(0, color='grey', linewidth=1)
for _, row in Dir1.iterrows():
    ax[0].plot([0, row['FPKM']], [row['Gene'], row['Gene']], color='grey', alpha=0.8, linewidth=1.2)

# Remove y-axis labels for the scatter plot
ax[0].set_yticklabels([])

# Plot B (Colorbar)
# Create a colormap
viridis_cmap = plt.cm.get_cmap('viridis', 10)
colorbar_img = np.array([Dir1['FPKM'].values])
sns.heatmap(colorbar_img, cmap=viridis_cmap, cbar=False, ax=ax[1])
ax[1].set_visible(False)  # Hide the second subplot but keep for spacing

plt.suptitle("This is good.", fontsize=14)
plt.tight_layout()
plt.show()

# Create a bidirectional color scale with RdBu reverse colormap

norm = TwoSlopeNorm(vmin=Dir2.log2FC.min(), vcenter=0, vmax=Dir2.log2FC.max())
cmap = cm.get_cmap('RdBu_r')

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Scatter plot with segments
for _, row in Dir2.iterrows():
    ax.plot([0, row['log2FC']], [row['Gene'], row['Gene']], color='grey', alpha=0.8, linewidth=1.2)
    ax.scatter(row['log2FC'], row['Gene'], c=[cmap(norm(row['log2FC']))], s=100, edgecolor='black')

ax.axvline(0, color='black', linewidth=1)  # Vertical line at x=0
ax.set_ylabel('Gene')
ax.set_xlabel('log2FC')
ax.set_title('Lightest color = 0\nDarkest colors = Max absolutes')

# Add a colorbar
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, orientation='vertical')

plt.show()

# good example 3

#Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Vertical line at x=0
ax.axvline(0, color='black', linewidth=1)

# Scatter plot with segments
for _, row in Dir3.iterrows():
    ax.plot([0, row['z.score']], [row['Gene'], row['Gene']], color='grey', alpha=0.8, linewidth=1.2)
    ax.scatter(row['z.score'], row['Gene'], c=[row['z.score']], cmap='YlGnBu', s=100, edgecolor='black', vmin=Dir3['z.score'].min(), vmax=Dir3['z.score'].max())

ax.set_ylabel('Gene')
ax.set_xlabel('z score')
ax.set_title('Darkest color = Max\nLightest color = Min')

# Add a colorbar
norm = TwoSlopeNorm(vmin=Dir3['z.score'].min(), vcenter=0, vmax=Dir3['z.score'].max())
sm = ScalarMappable(cmap='YlGnBu', norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, orientation='vertical')

plt.show()

## cannot create 4th figure bad example