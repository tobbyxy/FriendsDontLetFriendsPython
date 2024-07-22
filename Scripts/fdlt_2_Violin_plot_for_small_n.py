import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seed
np.random.seed(666)

# Generate data
data_set = pd.DataFrame(np.random.normal(1, 1, (5, 3)), columns=['V1', 'V2', 'V3'])

# Melt the DataFrame to long format
data_set = data_set.melt(var_name='sample', value_name='Response')

# Replace 'V' with 'group' in the 'sample' column
data_set['Group'] = data_set['sample'].str.replace('V', 'group')

# Display the first few rows
print(data_set.head())
# Fit the model
model_1 = smf.ols('Response ~ Group', data=data_set).fit()

# Perform ANOVA
print(anova_lm(model_1))

# Calculate the estimated marginal means
emmeans = model_1.fittedvalues

#Group means are clearly not different, as they are sampled from the same distribution

# Create a violin plot
violin_eg = sns.violinplot(x='Group', y='Response', data=data_set, palette='Accent', inner='point')

# Add a title
violin_eg.set_title('Points are median.', fontsize=12, color='black', weight='bold')

# Customize the axes and labels
violin_eg.set_xlabel('Group', fontsize=12, color='black', weight='bold')
violin_eg.set_ylabel('Response', fontsize=12, color='black', weight='bold')

# Add a caption
violin_eg.text(x=0.5, y=-0.2, s="The distributions are different!\nI wonder what's going on.", ha='center', va='center', transform=violin_eg.transAxes, fontsize=12)

# Show the plot
plt.show()

##Box plot
# Create a box plot
box_eg = sns.boxplot(x='Group', y='Response', data=data_set, palette='Accent')

# Add a title
box_eg.set_title('Boxes span IQR.', fontsize=12, color='black', weight='bold')

# Customize the axes and labels
box_eg.set_xlabel('Group', fontsize=12, color='black', weight='bold')
box_eg.set_ylabel('Response', fontsize=12, color='black', weight='bold')

# Add a caption
box_eg.text(x=0.5, y=-0.2, s="The quartiles are different!\nI wonder what's going on.", ha='center', va='center', transform=box_eg.transAxes, fontsize=12)


# Display the plot
plt.show()

##Strip plot

# Create a strip plot
jitter_eg = sns.stripplot(x='Group', y='Response', data=data_set, palette='Accent', jitter=0.2, size=5, edgecolor='gray')

# Add a title
jitter_eg.set_title('n = 5', fontsize=12, color='black', weight='bold')

# Customize the axes and labels
jitter_eg.set_xlabel('Group', fontsize=12, color='black', weight='bold')
jitter_eg.set_ylabel('Response', fontsize=12, color='black', weight='bold')

# Add a caption
jitter_eg.text(x=0.5, y=-0.2, s="Never mind...\nToo little data to say anything.", ha='center', va='center', transform=jitter_eg.transAxes, fontsize=12)

# Display the plot
plt.show()


###putting everything together

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Violin plot
sns.violinplot(x='Group', y='Response', data=data_set, palette='Accent', ax=axs[0])
axs[0].set_title('Violin Plot')
axs[0].text(0.5, -0.2, "The distributions are different!\nI wonder what's going on.", ha='center', va='center', transform=axs[0].transAxes)

# Box plot
sns.boxplot(x='Group', y='Response', data=data_set, palette='Accent', ax=axs[1])
axs[1].set_title('Box Plot')
axs[1].text(0.5, -0.2, "The quartiles are different!\nI wonder what's going on.", ha='center', va='center', transform=axs[1].transAxes)

# Jitter plot
sns.stripplot(x='Group', y='Response', data=data_set, palette='Accent', jitter=0.2, size=5, edgecolor='gray', ax=axs[2])
axs[2].set_title('Jitter Plot')
axs[2].text(0.5, -0.2, "Never mind...\nToo little data to say anything.", ha='center', va='center', transform=axs[2].transAxes)

plt.tight_layout()
plt.savefig('./Figures/Violin_plot_for_small_n.pdf', format='pdf')
plt.savefig('./Figures/Violin_plot_for_small_n.png', format='png')