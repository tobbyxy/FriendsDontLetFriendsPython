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
#plt.show()
plt.savefig('./Figures/good1.png', format='png')

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

#plt.show()
plt.savefig('./Figures/good2.png', format='png')

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

#plt.show()
plt.savefig('./Figures/good3.png', format='png')

##  4th figure bad example

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

#plt.show()
plt.savefig('./Figures/bad.png', format='png')


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Step 1: Assuming Good1, Good2, Good3, Bad are already saved as images
# For demonstration, replace these paths with the actual paths to your saved images
image_paths = ['./Figures/Good1.png', './Figures/Good2.png', './Figures/Good3.png', './Figures/bad.png']

# Step 2: Create a 2x2 grid to display the images
fig, axs = plt.subplots(2, 2, figsize=(7.5, 7.5))

# Flatten the array of axes for easy iteration
axs_flat = axs.flatten()

# Step 3: Load and display each image in its respective subplot
for ax, img_path in zip(axs_flat, image_paths):
    img = mpimg.imread(img_path)
    ax.imshow(img)
    ax.axis('off')  # Hide axes ticks and labels

plt.tight_layout()
#plt.show()

# Optionally, save this combined figure
plt.savefig("./Figures/CombinedPlots.png", format='png', bbox_inches='tight', facecolor='white')