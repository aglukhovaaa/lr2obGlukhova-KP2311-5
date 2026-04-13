# 1 задание сделала с Вагизовой
import os
Anna_secret=os.environ['Anna_secret']
print(Anna_secret)

import os
Sec_Glukhova_1=os.environ['Sec_Glukhova_1']
print(Sec_Glukhova_1)

import os
Sec_Glukhova_2=os.environ['Sec_Glukhova_2']
print(Sec_Glukhova_2)

import os
Sec_Glukhova_3=os.environ['Sec_Glukhova_3']
print(Sec_Glukhova_3)


# #Общее задание
# #1
# #линейный способ
# from sympy import*
# k,T,C,L = symbols('k C T L')
# C_ost=100000
# Am_lst=[]
# C_ost_lst=[]
# for i in range(5):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C: 100000, T:5, L:0})
#   Am_lst.append(round(Am.subs({C: 100000, T:5, L:0}), 2))
#   C_ost_lst.append(round(C_ost, 2))
# print( 'Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #2
# #способ уменьшаемого остатка
# Aj=0
# C_ost=100000
# Am_lst_2=[]
# C_ost_lst_2=[]
# for i in range(5):
#   Am = k * 1/T * (C - Aj)
#   C_ost -= Am.subs({C: 100000, T:5, k:2})
#   Am_lst_2.append(round(Am.subs({C: 100000, T:5, k:2}), 2))
#   Aj += Am
#   C_ost_lst_2.append(round(C_ost, 2))
# print ('Am_lst_2:', Am_lst_2)
# print ('C_ost_lst_2', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas as pd
# Y = range(1, 6)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #3
# #линейный способ
# from sympy import *
# k, T, C, L = symbols('k T C L')
# C_ost = 30000
# Am_lst =[]
# C_ost_lst=[]
# for i in range(8):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C:30000, T:8, L:0})
#   Am_lst.append(round(Am.subs({C: 30000, T:8, L:0}),2))
#   C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #способ уменьшаемого остатка
# Aj=0
# C_ost = 30000
# Am_lst_2=[]
# C_ost_lst_2=[]
# for i in range(8):
#   Am = k*1/T*(C - Aj)
#   C_ost -= Am.subs({C:30000, T:8, k:2})
#   Am_lst_2.append(round(Am.subs({C:30000, T:8, k:2}), 2))
#   Aj += Am 
#   C_ost_lst_2.append(round(C_ost,2))
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas as pd
# Y = range(1, 9)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #визуализация
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
# plt.savefig('chart1.png')
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am2')
# plt.savefig('chart2.png')

# vals = Am_lst
# labels = [str(x) for x in range(1,9)]
# explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart3.png')

# vals =  Am_lst_2
# labels = [str(x) for x in range(1,9)]
# explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart4.png')
# plt.clf()

# plt.figure()
# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tframe = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
# tframe2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig('chart5.jpeg')
# plt.figure()
# plt.bar(tfame2['Y'], tfame2['Am_lst_2'])
# plt.savefig('chart6.jpeg')

# #Индивидуальное задание №2
# #линейный способ
# from sympy import *
# k, T, C, L = symbols('k T C L')
# C_ost = 50000
# Am_lst =[]
# C_ost_lst=[]
# for i in range(9):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C:50000, T:9, L:0})
#   Am_lst.append(round(Am.subs({C: 50000, T:9, L:0}),2))
#   C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #способ уменьшаемого остатка
# Aj=0
# C_ost = 50000
# Am_lst_2=[]
# C_ost_lst_2=[]
# for i in range(9):
#   Am = k*1/T*(C - Aj)
#   C_ost -= Am.subs({C:50000, T:9, k:2})
#   Am_lst_2.append(round(Am.subs({C:50000, T:9, k:2}), 2))
#   Aj += Am 
#   C_ost_lst_2.append(round(C_ost,2))
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas as pd
# Y = range(1, 10)
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #визуализация
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
# plt.savefig('chart7.png')
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am2')
# plt.savefig('chart8.png')

# vals = Am_lst
# labels = [str(x) for x in range(1, len(vals) + 1)]
# explode = tuple([0.1] * len(vals))
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart9.png')

# vals =  Am_lst_2
# labels = [str(x) for x in range(1, len(vals) + 1)]
# explode = tuple([0.1] * len(vals))
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart10.png')
# plt.clf()

# plt.figure()
# table1 = list(zip(Y, Am_lst))
# table2 = list(zip(Y, Am_lst_2))
# tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig('chart11.jpeg')
# plt.figure()
# plt.bar(tfame2['Y'], tfame2['Am_lst_2'])
# plt.savefig('chart12.jpeg')


#ЛР 3 общее задание
#2 задание
#Вариант 3
#линейный способ
from sympy import *
k, T, C, L = symbols('k T C L') #что это? - создаёт символьные переменные с именами k, T, C, L.
C_ost = 30000
Am_lst =[]
C_ost_lst=[]
for i in range(9):
  Am = (C-L)/T
  C_ost -= Am.subs({C:30000, T:9, L:0})
  Am_lst.append(round(Am.subs({C: 30000, T:9, L:0}),2))
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

#способ уменьшаемого остатка
Aj=0
C_ost = 30000
Am_lst_2=[]
C_ost_lst_2=[]
for i in range(7):
  Am = k*1/T*(C - Aj)
  C_ost -= Am.subs({C:30000, T:7, k:2}) #что это? - формула ежегодного уменьшения остаточной стоимости основного средства на сумму начисленной амортизации.
  Am_lst_2.append(round(Am.subs({C:30000, T:9, k:2}), 2))
  Aj += Am 
  C_ost_lst_2.append(round(C_ost,2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер табличного вывода
import pandas as pd
Y = range(1, 8)
table1 = list(zip(Y, C_ost_lst, Am_lst)) #что это? - создаёт список кортежей, где каждый кортеж содержит значения из соответствующих списков Y, C_ost_lst и Am_lst.
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
print(tfame)
print(tfame2)

#визуализация
import numpy as np
import matplotlib.pyplot as plt
plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
plt.savefig('chart7.png') #что это? - сохраняет текущую фигуру в файл с именем 'chart7.png'  
plt.figure()
plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am2')
plt.savefig('chart8.png')
plt.figure()

vals = Am_lst
labels = [str(x) for x in range(1, len(vals) + 1)]
explode = tuple([0.1] * len(vals))
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
ax.axis("equal")
plt.savefig('chart9.png')
plt.figure() #что это? - создаёт новую фигуру для построения графиков.

vals =  Am_lst_2
labels = [str(x) for x in range(1, len(vals) + 1)]
explode = tuple([0.1] * len(vals))
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
ax.axis("equal")
plt.savefig('chart10.png')
plt.clf()
plt.figure()

table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst']) #что это? - создаёт DataFrame из списка кортежей таблицу table1 с указанными именами столбцов.
tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
plt.bar(tfame['Y'], tfame['Am_lst'])
plt.savefig('chart11.jpeg')
plt.figure()
plt.bar(tfame2['Y'], tfame2['Am_lst_2'])
plt.savefig('chart12.jpeg')
plt.figure()
#Внесены изменения в данные варианта
#Проверила Романова Елизавета, оценка 5/5
#Романова Елизавета ответила на вопросы верно! 5/5! 

