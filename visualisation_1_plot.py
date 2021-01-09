import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('visualisation_1.csv')

cols = df.columns[1:6]

ax = plt.gca()
for col in cols:
    df.plot(kind='line',x='Week',y=col,ax=ax)

plt.show()