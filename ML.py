# from sklearn.datasets import load_boston
# from sklearn.linear_model import LinearRegression, Ridge, Lasso
from math import  sqrt
# boston =  load_boston()

# x = boston.data
# y = boston.target

# lr1 = LinearRegression()
# lr1.fit(x, y)

# print("Linear Regression")

# for f, w in zip(boston.feature_names, lr1.coef_):
#     print("{0:7s}:{1:6.2f}".format(f,w))
# print("coef = {0:4.2f}".format(sum(lr1.coef_**2)))

# P1 = [5,5,5,3]
# P2 = [5,3,4,4]
# P3 = [2,5,3,5]
# P4 = [3,4,4,None]

# P1P4 = abs(P1[0] - P4[0]) + abs(P1[1] - P4[1]) + abs(P1[2] - P4[2])
# P2P4 = abs(P2[0] - P4[0]) + abs(P2[1] - P4[1]) + abs(P2[2] - P4[2])
# P3P4 = abs(P3[0] - P4[0]) + abs(P3[1] - P4[1]) + abs(P3[2] - P4[2])

# print(P1P4, P2P4, P3P4, sep='\n')

# P4[3] = (1/(1/P1P4 + 1/P2P4 + 1/P3P4)) * (P1[3]/P1P4 + P2[3]/P2P4 + P3[3]/P3P4)
# print(P4)

# a = sqrt(1+1+1) 
# print(a)

# a = (19 - 15)**2
# print(a)
# def manhet(list1, list2, list3, list4):
#     s = 0
#     for a, b, c, d in zip(list1, list2, list3, list4):
#         s += abs(a - b) + abs(a - c) + abs(a - d)
#     return s

# a = [1, 1, 0]
# b = [0, 2, -1]
# c = [2, 3, 1]
# d = [1, 0, 4]

# print('a:', manhet(a, b, c, d))
# print('b:', manhet(b, c, d, a))
# print('c:', manhet(c, b, a, d))
# print('d:', manhet(d, b, c, a))

# a = [0, 3, 4, 4, 1] 
# b = [3, 0, 1 ,2, 5]
# c = [4, 1, 0, 3, 3]
# d = [3, 2, 3, 0, 4]
# e = [1, 5, 3, 4, 0]

# def dist(list1, list2):
#     s = 0
#     for i in range(len(list1)):
#         s += abs(list1[i] - list2[i])
#     return (s ** 0.5)
    
# print('a to b', dist(a, b))
# print('a to c', dist(a, c))
# print('a to d', dist(a, d))
# print('a to e', dist(a, e))

# import matplotlib.pyplot as plt


# p1 = [4, 3, 1, -1, 0]
# p2 = [2, 2, -1, 1, 4]
# center = [1, 2]
# r = 2.5
# # plot
# fig, ax = plt.subplots()
# ax.plot(p1, p2, 'bo')
# ax.plot(center[0], center[1], 'ro')
# plt.show()

# def mae_mape(list1, list2):
#     s = 0
#     s1 = 0
#     for i, j in zip(list1, list2):
#         s += abs(i - j)
#         s1 += abs(i - j) / abs(i)
#     print('mae:', s / len(list1), '\n', 'mape:', (s1 / len(a)) * 100)

# a = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
# b = [0, 2, 2, 5, 3, -1, -1, -4, -6, -5]

# mae_mape(a, b)

# print(15/25)

Gini = 3/5*2/5*3/5
print(Gini)