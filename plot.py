import pandas as pd
import matplotlib.pyplot as plt

var = pd.read_excel("data_recorder.xlsx")
# print(var)


x = list(var['time'])
y = list(var['buy_price'])

plt.plot(y)

plt.show()