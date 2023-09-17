'''
@File    :   genedata.py
@Time    :   2023/09/17 10:41:30
@Author  :   Ming 
'''

import numpy as np
import matplotlib.pyplot as plt

zone_list = [f"Zone {i}" for i in range(1, 7)]


def logistic_increase_function(t, K, P0, r):
  # t:time   t0:initial time    P0:initial_value    K:capacity  r:increase_rate
  exp_value = np.exp(r * (t - 10))
  return (K * exp_value * P0) / (K + (exp_value - 1) * P0)


def generate(K, r):
  _list = []
  for t in range(100):
    _list.append(round(logistic_increase_function(t, K, 5, r)))
  return _list


data1 = generate(8000, 0.15)
data2 = generate(4000, 0.15)
data3 = generate(8000, 0.08)
data4 = generate(8000, 0.1)
data5 = generate(4000, 0.1)
data6 = generate(8000, 0.2)
plt.plot(data1)
plt.plot(data2)
plt.plot(data3)
plt.plot(data4)
plt.plot(data5)
plt.plot(data6)
plt.show()

# data1 = np.cumsum(np.random.randint(low=10 * 1.1, high=40 * 1.1, size=(100,)))
# data2 = np.cumsum(np.random.randint(low=10 * 1.3, high=40 * 1.3, size=(100,)))
# data3 = np.cumsum(np.random.randint(low=10 * 2.3, high=40 * 2.3, size=(100,)))
# data4 = np.cumsum(np.random.randint(low=10 * 1.7, high=40 * 1.7, size=(100,)))
# data5 = np.cumsum(np.random.randint(low=10 * 0.4, high=40 * 0.4, size=(100,)))
# data6 = np.cumsum(np.random.randint(low=10 * 3, high=40 * 3, size=(100,)))

date = list(range(1, 101))
for date in date:
  print([data1[date - 1], zone_list[0], date], end=',')
  print([data2[date - 1], zone_list[1], date], end=',')
  print([data3[date - 1], zone_list[2], date], end=',')
  print([data4[date - 1], zone_list[3], date], end=',')
  print([data5[date - 1], zone_list[4], date], end=',')
  print([data6[date - 1], zone_list[5], date], end=',')
