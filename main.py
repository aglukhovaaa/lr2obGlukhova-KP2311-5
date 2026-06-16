# # Общее 1 задание сделала с Вагизовой Камиллой
# import os
# Anna_secret=os.environ['Anna_secret']
# print(Anna_secret)

# import os
# Sec_Glukhova_1=os.environ['Sec_Glukhova_1']
# print(Sec_Glukhova_1)

# import os
# Sec_Glukhova_2=os.environ['Sec_Glukhova_2']
# print(Sec_Glukhova_2)

# import os
# Sec_Glukhova_3=os.environ['Sec_Glukhova_3']
# print(Sec_Glukhova_3)


# #ЛР 3 общее задание, 3 вариант
# #линейный способ
# from sympy import *
# k, T, C, L = symbols('k T C L') #что это? - создаёт символьные переменные с именами k, T, C, L.
# C_ost = 40000
# Am_lst =[]
# C_ost_lst=[]
# for i in range(10):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C:40000, T:10, L:0})
#   Am_lst.append(round(Am.subs({C: 40000, T:10, L:0}),2))
#   C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #способ уменьшаемого остатка
# Aj=0
# C_ost = 40000
# Am_lst_2=[]
# C_ost_lst_2=[]
# for i in range(9):
#   Am = k*1/T*(C - Aj)
#   C_ost -= Am.subs({C:40000, T:10, k:2}) #что это? - формула ежегодного уменьшения остаточной стоимости основного средства на сумму начисленной амортизации.
#   Am_lst_2.append(round(Am.subs({C:40000, T:10, k:2}), 2))
#   Aj += Am 
#   C_ost_lst_2.append(round(C_ost,2))
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного вывода
# import pandas as pd
# Y = range(1, 11)
# table1 = list(zip(Y, C_ost_lst, Am_lst)) #что это? - создаёт список кортежей, где каждый кортеж содержит значения из соответствующих списков Y, C_ost_lst и Am_lst.
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
# tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
# print(tfame)
# print(tfame2)

# #визуализация
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
# plt.savefig('chart7.png') #что это? - сохраняет текущую фигуру в файл с именем 'chart7.png'  
# plt.figure()
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am2')
# plt.savefig('chart8.png')
# plt.figure()

# vals = Am_lst
# labels = [str(x) for x in range(1, len(vals) + 1)]
# explode = tuple([0.1] * len(vals))
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.savefig('chart9.png')
# plt.figure() #что это? - создаёт новую фигуру для построения графиков.

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
# tfame = pd.DataFrame(table1, columns=['Y', 'Am_lst']) #что это? - создаёт DataFrame из списка кортежей таблицу table1 с указанными именами столбцов.
# tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_lst_2'])
# plt.bar(tfame['Y'], tfame['Am_lst'])
# plt.savefig('chart11.jpeg')
# plt.figure()
# plt.bar(tfame2['Y'], tfame2['Am_lst_2'])
# plt.savefig('chart12.jpeg')
# plt.figure()

# #Внесены изменения в данные варианта
# #Проверила Романова Елизавета, оценка 5/5
# #Романова Елизавета ответила на вопросы верно! 5/5! 

# #Индивидуальное задание
# #Вариант 2 "Защита гипервизора от несанкционированного доступа из физической сети"
# #1. Для определенных в ТЗ компонентов интеграции создать в реплике необходимое количество секретных ключей
# import os
# CONTAINER_SIGNING_KEY=os.environ['CONTAINER_SIGNING_KEY']
# print(CONTAINER_SIGNING_KEY)

# import os
# FILTER_RULES_SECRET=os.environ['FILTER_RULES_SECRET']
# print(FILTER_RULES_SECRET)

# import os
# HYPERVISOR_AUTH_TOKEN=os.environ['HYPERVISOR_AUTH_TOKEN']
# print(HYPERVISOR_AUTH_TOKEN)

# import os
# MONITORING_API_KEY=os.environ['MONITORING_API_KEY']
# print(MONITORING_API_KEY)

# #2. В реплике напишите код контейнеров расчета, табличного представления результатов и визуализации результатов для одного микросервиса по варианту индивидуального задания из ЛР1, согласно ТЗ. Запустите реплику и оцените результаты работы контейнеров расчета, табличного представления результатов и визуализации результатов.

# import pandas as pd
# import matplotlib.pyplot as plt


# incoming = [850, 1200, 5000, 8500, 12000, 15000, 8000, 3000, 1500, 900] # Входящий трафик (пакетов в секунду)
# attempts = [5, 8, 45, 78, 120, 165, 85, 25, 8, 3] # Попытки несанкционированного доступа
# threshold = 4500  # Порог срабатывания (пакетов/с)
# base_filter = 95  # Базовый уровень фильтрации (%)
# koef = 2.5        # Коэффициент усиления при атаке

# blocked = []      # Заблокированные пакеты
# efficiency = []   # Эффективность (%)
# risk = []         # Остаточный риск (%)
# filter_level = [] # Уровень фильтрации (%)

# for i in range(10):
#   if incoming[i] > threshold:
#           anomaly = (incoming[i] - threshold) / threshold

#           current_filter = base_filter + (anomaly * 100 * koef)
#           if current_filter > 99.5:
#               current_filter = 99.5
#   else:
#           anomaly = 0
#           current_filter = base_filter
#   filter_level.append(round(current_filter, 1))
#   blocked_count = incoming[i] * (current_filter / 100)
#   blocked.append(round(blocked_count, 0))

#   eff = (blocked_count / incoming[i]) * 100
#   efficiency.append(round(eff, 1))

#   r = 100 - eff
#   risk.append(round(r, 1))

#   blocked_attempts = attempts[i] * (current_filter / 100)

# Y = list(range(1, 11))  # Номера интервалов
# C_ost_lst = risk        # Остаточный риск
# Am_lst = efficiency     # Эффективность

# print('blocked:', blocked)
# print('efficiency:', efficiency)
# print('risk:', risk)
# print('filter_level:', filter_level)


# #Табличное представление
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
# print(tfame)

# table2 = list(zip(Y, incoming, blocked, filter_level))
# tfame2 = pd.DataFrame(table2, columns=['Y', 'Incoming', 'Blocked', 'Filter_%'])
# print(tfame2)


# #Визуализация
# plt.plot(tfame['Y'], tfame['C_ost_lst'], 'b-o', linewidth=2, markersize=8, label='Остаточный риск')
# plt.xlabel('Интервал')
# plt.ylabel('Риск (%)')
# plt.title('Остаточный риск защиты гипервизора')
# plt.legend()
# plt.grid(True)
# plt.savefig('chart13.png')
# plt.figure()

# plt.plot(tfame['Y'], tfame['Am_lst'], 'r-s', linewidth=2, markersize=8, label='Эффективность')
# plt.xlabel('Интервал')
# plt.ylabel('Эффективность (%)')
# plt.title('Эффективность защиты гипервизора')
# plt.legend()
# plt.grid(True)
# plt.savefig('chart14.png')
# plt.figure()

# vals = Am_lst
# labels = [str(x) for x in range(1, len(vals) + 1)]
# explode = tuple([0.1] * len(vals))
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, 
#        wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.title('Распределение эффективности')
# plt.savefig('chart15.png')
# plt.figure()

# vals = C_ost_lst
# labels = [str(x) for x in range(1, len(vals) + 1)]
# explode = tuple([0.1] * len(vals))
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode,
#        wedgeprops={'lw':1, 'ls':'--', 'edgecolor':"k"}, rotatelabels=True)
# ax.axis("equal")
# plt.title('Распределение остаточного риска')
# plt.savefig('chart16.png')
# plt.clf()
# plt.figure()

# table_eff = list(zip(Y, Am_lst))
# tfame_eff = pd.DataFrame(table_eff, columns=['Y', 'Am_lst'])
# plt.bar(tfame_eff['Y'], tfame_eff['Am_lst'])
# plt.xlabel('Интервал')
# plt.ylabel('Эффективность (%)')
# plt.title('Эффективность защиты (столбцы)')
# plt.savefig('chart17.jpeg')
# plt.figure()

# table_risk = list(zip(Y, C_ost_lst))
# tfame_risk = pd.DataFrame(table_risk, columns=['Y', 'C_ost_lst'])
# plt.bar(tfame_risk['Y'], tfame_risk['C_ost_lst'], color='orange')
# plt.xlabel('Интервал')
# plt.ylabel('Риск (%)')
# plt.title('Остаточный риск (столбцы)')
# plt.savefig('chart18.jpeg')
# plt.figure()



#ЛР6 ОБЩЕЕ ЗАДАНИЕ

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 5])
plt.ylabel('some numbers')
plt.savefig('example.png')

from sklearn.datasets import make_blobs
import pandas as pd
dataset, classes = make_blobs(n_samples=200, n_features=2,
centers=4, cluster_std=0.5, random_state=0)
df = pd.DataFrame(dataset, columns=['var1', 'var2'])
print(df.head(2))

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Генерация данных
dataset, classes = make_blobs(n_samples=200, n_features=2,
                              centers=4, cluster_std=0.5, random_state=0)
df = pd.DataFrame(dataset, columns=['var1', 'var2'])
print(df.head(2))

inertias = []
k_range = range(2, 13)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=0, n_init=10)
    kmeans.fit(df)
    inertias.append(kmeans.inertia_)

# Построение графика метода локтя
plt.figure(figsize=(8, 6))
plt.plot(k_range, inertias, 'bo-')
plt.xlabel('Количество кластеров (k)')
plt.ylabel('Инерция')
plt.title('Метод локтя для определения оптимального k')
plt.grid(True)
plt.savefig("elbow_method.png", dpi=150, bbox_inches="tight")
plt.show()

print(f"Инерции для k от 2 до 12: {inertias}")

kmeans = KMeans(n_clusters=4, init='k-means++',
random_state=0).fit(df)
print(kmeans. labels_)
print(kmeans. cluster_centers_)
print(kmeans. inertia_)
print(kmeans.n_iter_)

from collections import Counter
Counter(kmeans.labels_)
print(Counter(kmeans.labels_))

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="var1", y="var2", hue=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker="X", c="r", s=80, label="centroids")
plt.savefig("clusters.png", dpi=150, bbox_inches="tight")
plt.legend()
plt.show()


#Индивидуальное задание, 2 Вариант 
# Блок импорта библиотек
from sklearn.cluster import KMeans
from collections import Counter
import pandas as pd
import numpy as np
import sklearn
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import os
# Блок проверки версии scikit-learn
print("scikit-learn version:", sklearn.__version__)
# Блок генерации исходных данных по индивидуальному варианту №2
# Фиксируем генератор случайных чисел, чтобы при каждом запуске
# данные генерировались одинаково
np.random.seed(0)
# Количество записей в массиве M
n_samples = 200
# Первый параметр изменяется в диапазоне [0.01; 1]
param1 = np.random.uniform(0.01, 1, n_samples)
# Второй параметр изменяется в диапазоне [1; 300]
param2 = np.random.uniform(1, 300, n_samples)
# Третий параметр принимает значения: Самара, Тольятти, Москва
cities = np.random.choice(
    ["Самара", "Тольятти", "Москва"],
    size=n_samples
)
# Формируем исходную таблицу данных
df = pd.DataFrame({
    "param1": param1,
    "param2": param2,
    "city": cities
})
print("Исходные данные:")
print(df.head(10))
# Блок преобразования категориального признака
# Алгоритм KMeans работает только с числовыми данными.
# Поэтому города кодируем числами:
# Самара = 0, Тольятти = 1, Москва = 2
city_codes = {
    "Самара": 0,
    "Тольятти": 1,
    "Москва": 2
}
# Создаём отдельный числовой столбец city_code
df["city_code"] = df["city"].map(city_codes)
print("\nДанные после кодирования городов:")
print(df.head(10))
# Блок подготовки данных для кластеризации
# Для обучения модели берём только числовые признаки:
# param1, param2 и city_code
M = df[["param1", "param2", "city_code"]]
print("\nМассив M для кластеризации:")
print(M.head(10))
# Блок настройки и обучения модели KMeans
# Создаём модель KMeans
# n_clusters=3, так как третий параметр принимает 3 значения:
# Самара, Тольятти, Москва
# init="k-means++" — улучшенный метод выбора начальных центроидов
# random_state=0 — фиксация результата
# n_init=10 — количество запусков алгоритма с разными начальными центрами
kmeans = KMeans(
    n_clusters=3,
    init="k-means++",
    random_state=0,
    n_init=10
).fit(M)
# Блок вывода результатов кластеризации
# Метки кластеров для каждой записи
print("\nПрогнозируемые кластеры для каждой записи:")
print(kmeans.labels_)
# Координаты центроидов кластеров
print("\nКоординаты центроидов:")
print(kmeans.cluster_centers_)
# Внутрикластерная сумма квадратов
print("\nВнутрикластерная сумма квадратов inertia:")
print(kmeans.inertia_)
# Количество итераций алгоритма KMeans
print("\nКоличество итераций:")
print(kmeans.n_iter_)
# Размер каждого кластера
print("\nРазмер каждого кластера:")
print(Counter(kmeans.labels_))
# Блок добавления результатов кластеризации в таблицу
# Добавляем в таблицу новый столбец cluster
# Он показывает, к какому кластеру отнесена каждая запись
df["cluster"] = kmeans.labels_
print("\nТаблица с результатами кластеризации:")
print(df.head(10))
# Блок визуализации кластеров
# Создаём область графика
plt.figure(figsize=(9, 6))
# Строим диаграмму рассеяния:
# по оси X — первый параметр
# по оси Y — второй параметр
# цвет точки — номер найденного кластера
# style="city" дополнительно различает города разными маркерами
sns.scatterplot(
    data=df,
    x="param1",
    y="param2",
    hue="cluster",
    style="city",
    palette="viridis",
    s=80
)
# Отображаем центроиды кластеров.
# Берём только первые две координаты центроидов,
# потому что график двумерный: param1 и param2
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker="X",
    c="r",
    s=150,
    label="centroids"
)
# Блок оформления графика
plt.title("KMeans Clustering: Самара, Тольятти, Москва")
plt.xlabel("Параметр 1 [0.01; 1]")
plt.ylabel("Параметр 2 [1; 300]")
plt.legend()
# Блок сохранения графика в файл Replit
# В Replit plt.show() часто не открывает окно,
# поэтому график сохраняется как изображение
plt.savefig(
    "/home/runner/workspace/individual_clusters.png",dpi=150,bbox_inches="tight")
plt.close()
# Блок проверки создания файла
print("\nТекущая папка:", os.getcwd())
print("Файл individual_clusters.png создан:",os.path.exists("/home/runner/workspace/individual_clusters.png"))
print("График сохранён в файл individual_clusters.png")



                              