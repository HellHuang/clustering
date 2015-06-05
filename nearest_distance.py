# coding=utf-8
import re
'''该层次聚类针对于bank-data的数据集，不具有一般性，不过能很好体现层次的思想'''
'''计算距离矩阵'''
def distance(attr, i, j,min_age,max_age,min_kid,max_kid,min_income,max_income):
    temp_i = attr[i].strip().split(',')
    temp_j = attr[j].strip().split(',')
    '''数值归一化'''
    at_i1 = (int(temp_i[1]) * 1.0 - min_age) / (max_age - min_age + 1)
    at_j1 = (int(temp_j[1]) * 1.0 - min_age) / (max_age - min_age + 1)
    at_ij1 = abs(at_i1 - at_j1)
    at_ij2 = 1
    if (temp_i[2] == temp_j[2]):
        at_ij2 = 0
    at_ij3 = 1
    if (temp_i[3] == temp_j[3]):
        at_ij3 = 0
    '''数值归一化'''
    at_i4 = (float(temp_i[4]) * 1.0 - min_income) / (max_income - min_income + 1)
    at_j4 = (float(temp_j[4]) * 1.0 - min_income) / (max_income - min_income + 1)
    at_ij4 = abs(at_i4 - at_j4)
    at_ij5 = 1
    if (temp_i[5] == temp_j[5]):
        at_ij5 = 0
    '''数值归一化'''
    at_i6 = (float(temp_i[6]) * 1.0 - min_kid) / (max_kid - min_kid + 1)
    at_j6 = (float(temp_j[6]) * 1.0 - min_kid) / (max_kid - min_kid + 1)
    at_ij6 = abs(at_i6 - at_j6)
    at_ij7 = 1
    if (temp_i[7] == temp_j[7]):
        at_ij7 = 0
    at_ij8 = 1
    if (temp_i[8] == temp_j[8]):
        at_ij8 = 0
    at_ij9 = 1
    if (temp_i[9] == temp_j[9]):
        at_ij9 = 0
    at_ij10 = 1
    if (temp_i[10] == temp_j[10]):
        at_ij10 = 0
    at_ij11 = 1
    if (temp_i[11] == temp_j[11]):
        at_ij11 = 0
    d = at_ij1 + at_ij2 + at_ij3 + at_ij4 + at_ij5 + at_ij6 + at_ij7 + at_ij8 + at_ij9 +at_ij10+ at_ij11
    return d

'''读取csv文件'''
def DataIscsv(filename):
    file_object = open(filename, 'r')
    line = file_object.readlines()
    len=line.__len__()
    file_object = open(filename, 'r')
    attr = []
    line = file_object.readline()
    line.replace('\n', '')
    max_age = -1
    min_age = 99999
    max_kid = -1
    min_kid = 99999
    max_income = -1
    min_income = 999999
    while line:
        line = file_object.readline()
        if line:
            temp = line.strip().split(',')
            tem_age = int(temp[1])
            tem_income = float(temp[4])
            tem_kid = int(temp[6])
            if tem_age > max_age:
                max_age = tem_age
            if tem_age < min_age:
                min_age = tem_age
            if tem_income > max_income:
                max_income = tem_income
            if tem_income < min_income:
                min_income = tem_income
            if tem_kid > max_kid:
                max_kid = tem_kid
            if tem_kid < min_kid:
                min_kid = tem_kid
            attr.append(line)
    value = [[0 for col in range(0, len-1, 1)] for row in range(0,len-1, 1)]
    for i in range(0, len-1, 1):
        for j in range(i, len-1, 1):
            value[i][j]=distance(attr, i, j,min_age,max_age,min_kid,max_kid,min_income,max_income)
            value[j][i]=value[i][j]
    return value


class K_means():			# K_means算法 需要参数 number of clusters

    def __init__(self, k):
        info=DataIscsv('bank-data.csv')
        weights = []
        vx=info.__len__()
        center = [[1, info[i]] for i in range(k)]
        resultk = [[i] for i in range(k)]
        width = len(info[0])
        for i in range(k, len(info)):
            min_center = self.min_dis_center(center, info[i])
            for j in range(width):
                center[min_center][1][j] = (center[min_center][1][j] * center[min_center][0] + info[i][j])/ (1.0+center[min_center][0])
            center[min_center][0] += 1
            resultk[min_center].append(i)
        self.result = resultk
        #self.Q = aaa.CountQQ(self.result, data)
        a = [0 for i in range(vx)]
        for i in range(0, self.result.__len__(), 1):
            for j in range(0, self.result[i].__len__(), 1):
                a[self.result[i][j]] = i
        self.listresult = a

    def GetResult(self):
        return self.result,  self.listresult

    def fun_dis(self, x, y, n):
        return sum(map(lambda v1, v2: pow(abs(v1-v2), n), x, y))

    def distance(self, x, y):
        return self.fun_dis(x, y, 2)

    def min_dis_center(self, center, node):
        min_index = 0
        min_dista = self.distance(center[0][1], node)
        for i in range (1, len(center)):
            tmp = self.distance(center[i][1], node)
            if tmp < min_dista:
                min_dista = tmp
                min_index = i
        return min_index
kmeans=K_means(5)
result=kmeans.GetResult()
print result[0].__len__()
for i in result[0]:
    print i

