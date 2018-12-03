import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('NYC_Jobs.csv')
names = ['Agency', '# Of Positions']
print(df[names])
df['Agency'].value_counts(sort = True).plot.bar()
plt.show()
