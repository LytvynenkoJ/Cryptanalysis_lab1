import numpy as np
import pandas as pd

#завантажуємо інформацію з файлів
prob_data = pd.read_csv('prob_14.csv',delimiter=',', header=None)
table_data = pd.read_csv('table_14.csv',delimiter=',', header=None)
print(prob_data)
print(table_data)

#будуємо таблицю розподілу ймовірностей P(M,C)
#для цього сумуємо P(M)*P(k) для всіх С по таким (M, k), що Е(M, k)=С
table_cm = [[0 for j in range(20)] for i in range(20)]
for i in range(20):
    for j in range(20):
        temp = prob_data[i][0]*prob_data[j][1]
        x = table_data[i][j]
        table_cm[x][i]+=temp
table_cm = np.array(table_cm)
print(table_cm)

#будуємо таблицю розподілу ймовірностей P(C)
#для кожного С сумуємо P(M, C) по всім M
prob_c=[0 for j in range(20)]
prob_c = np.array(prob_c, dtype=float)
for i in range(20):
    for j in range(20):
        prob_c[i] += table_cm[i][j]
print(prob_c)

#будуємо таблицю розподілу ймовірностей P(M|C)
#використовуємо формулу умовної ймовірності: P(M|C) = P(M,C)/P(C)
table_mc = [[0 for j in range(20)] for i in range(20)]
table_mc = np.array(table_mc, dtype=float)
for i in range(20):
    for j in range(20):
        table_mc[i][j]=table_cm[i][j]/prob_c[i]
print(table_mc)
