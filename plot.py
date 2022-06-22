from turtle import color
import pandas as pd
import matplotlib.pyplot as plt

var = pd.read_excel("data_recorder_ntpc_21_06.xlsx")
# print(var)


x = list(var['time'])
y = list(var['buy_price'])

# x.title("time")
plt.plot(y)
plt.xlabel("Time", color = "Red")
plt.ylabel("Price", color = "Red")

plt.show()