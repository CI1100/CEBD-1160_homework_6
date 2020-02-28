##1. Still using the same DataFrame from the previous exercise insurance.csv
#plot the chart for charges and save it as charges_plot.png
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np

insurance = pd.read_csv('insurance.csv', header=0)

os.makedirs('plots', exist_ok=True)

plt.plot(insurance['charges'], color='blue')
plt.title('Charges')
plt.ylabel('Charges')
plt.savefig(f'plots/charges_plot.png', format='png')
plt.show()
plt.clf()

##2. plot the histogram for bmi and save it as bmi_hist.png
plt.hist(insurance['bmi'], bins=3, color='g')
plt.title('BMI')
plt.xlabel('Bmi')
plt.ylabel('Count')
plt.savefig(f'plots/bmi_hist.png', format='png')
plt.show()
plt.clf()

##3.plot the scatterplot for age vs charges and save it as age_charge_scatter.png
plt.scatter(insurance['age'], insurance['charges'], color='b')
plt.title('Age to Charges')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.savefig(f'plots/age_vs_charges.png', format='png')
plt.show()
plt.close()

##4.Re-do the previous items, adding the title, x label and y label for each item.
##5.Think about the exercise 12 from the previous section. Do the plots match what we saw with the correlation function?
matrix = np.triu(insurance.corr())
sns.heatmap(insurance.corr(), annot = True, vmin=-1, vmax=1, center= 0, cmap= 'coolwarm', mask=matrix)
plt.legend(['Correlation'])
plt.savefig('plots/correlation_seaborn.png')