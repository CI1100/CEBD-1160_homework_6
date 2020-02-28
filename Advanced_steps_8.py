import matplotlib.pyplot as plt
import pandas as pd
import os

df = pd.read_csv('CEBD-1160_homework_6/wine.data', sep=',', header=0)

plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

# This time we plot multiple plots on the same axes, to get some perspective on their comparisons
axes.scatter(df['Alcohol'], df['Total phenols'], alpha=0.7, label='Total Phenols')
axes.scatter(df['Alcohol'], df['Color intensity'], alpha=0.7, label='Color Intensity')
axes.scatter(df['Alcohol'], df['Malic acid'], alpha=0.7, label='Malic Acid')

axes.set_xlabel('Alcohol')
axes.set_ylabel('Total Phenols / Color Intensity')
axes.set_title(f'Alcohol comparisons')
axes.legend()
plt.savefig(f'CEBD-1160_homework_6/plots_8/multiplot_scatter.png', dpi=300)

plt.close()
