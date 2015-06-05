__author__ = 'fen'
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

'''层次聚类'''
def hi_clustering(value):
    node = [[0 for col in range(0, 2, 1)] for row in range(0,value.__len__(), 1)]
    for i in range(0,value.__len__(),1):
        node[i][0]=-1
        node[i][1]='%s'%i
    list=[]
    while(1):
        mergelist=[]
        for i in range(0,value.__len__(),1):
            merge=[]
            if value[i][i] == -1:
                continue
            min= 9999
            k=-1
            for j in range(i+1,value.__len__(),1):
                if value[j][j]== -1:
                    continue
                if value[i][j] < min and node[j][0] == -1:
                    min = value[i][j]
                    k = j
            # print k
            if k > -1:
                for p in range(0,value.__len__(),1):
                    value[i][p]=(value[i][p]+value[k][p])/2
                    value[k][p]=-1
                node[i][1] =node[i][1]+','+node[k][1]
                node[i][0] = 1
                node[k][0] = 1
        for p in range(0,value.__len__(),1):
            if value[p][p]== -1:
                continue
            mergelist.append(node[p][1])
        for p in range(0,value.__len__(),1):
            if value[p][p]== -1:
                continue
            node[p][0]=-1
        list.append(mergelist)
        count=0
        for t in range(0,value.__len__(),1):
            if value[t][t]== -1:
                count =count + 1
        if count == value.__len__() - 1 :
            break
    return list


if __name__ == "__main__":
    filename = "bank-data.csv"
    value=DataIscsv(filename)
    print value.__len__()
    list=hi_clustering(value)
    for li in list:
        print li
    print list.__len__()
    # print node[0]