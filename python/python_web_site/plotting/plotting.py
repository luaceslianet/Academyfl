import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\portfolio\Academyfl\python\python_web_site\plotting\data.csv')

df.plot()

plt.show()

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()