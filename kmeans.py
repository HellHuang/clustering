__author__ = 'fen'
#coding=utf-8
import re
import random
import math
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



def print_matchs(matchs) :
    for i in range(len(matchs)) :
        print i , '---->',
        for item in matchs[i] :
            print item,
        print
    print '-'*200
def pearson_distance(vector1, vector2) :
    """
    Calculate distance between two vectors using pearson method
    """
    sum1 = sum(vector1)
    sum2 = sum(vector2)

    sum1Sq = sum([pow(v,2) for v in vector1])
    sum2Sq = sum([pow(v,2) for v in vector2])

    pSum = sum([vector1[i] * vector2[i] for i in range(len(vector1))])

    num = pSum - (sum1*sum2/len(vector1))
    den = math.sqrt((sum1Sq - pow(sum1,2)/len(vector1)) * (sum2Sq - pow(sum2,2)/len(vector1)))

    if den == 0 : return 0.0
    return 1.0 - num/den
def euclidean_distance(vector1, vector2) :
    p=0
    num=len(vector1)
    enclidean=0
    ''''for i in range(num):
        p+=(vector1[i]-vector2[i])*(vector1[i]-vector2[i])
        #p += sum ((vector1[i]-vector2[i])**2)'''
    p=sum([(vector1[i]-vector2[i])**2 for i in range(num)])

    #print p
    enclidean=math.sqrt(p)
    del p
    print enclidean
    return enclidean

def kmeans(matrix, k) :

    """generate k clusters randomly
    """
    clusters = [0 for i in range(k)]
    lastcluster=[0 for i in range(k)]
    min_=0
    max_=matrix.__len__()
    print "len",max_
    cluster = [0 for i in range(k)]
    for i in range(k) :

        cluster[i]=int(random.random() * (max_ - min_) + min_)
        clusters[i]=matrix[cluster[i]]
        lastcluster[i]=matrix[cluster[i]]
        #print cluster[i],clusters[i]

    lastmatchs = [ [] for i in range(k)]

    """ initial the round is 100"""
    rounds = 100
    while rounds > 0 :
        matchs = [ [] for i in range(k)]
        print 'round \t',rounds
        for i in range(len(matrix)) :
            bestmatch_cluster = None

            min_distance = 100000
            for j in range(k) :
                dis = pearson_distance(clusters[j], matrix[i])
                if dis < min_distance :
                    min_distance = dis
                    bestmatch_cluster = j
            matchs[bestmatch_cluster].append(i)

        print_matchs(matchs)
        #print_matchs(lastmatchs)



        if matchs == lastmatchs : break
        #if cluster== lastcluster :break
        lastmatchs = [[ item for item in matchs[i] ] for i in range(k)]

        #move the centroids to the average of their members
        for j in range(k) :
            avg = [0.0 for i in range(len(matrix[0])) ]
            for m in matchs[j] :
                vec = matrix[m]
                for i in range(len(matrix[0])) :
                    avg[i] += vec[i]
            avg = [ item / len(matrix[0]) for item in avg]
            clusters[j] = avg
        lastcluster=clusters


        rounds -= 1
    print "rounds:",100-rounds
    print "result:"
    for i in matchs:
        print i


if __name__ == '__main__' :

    matrix=DataIscsv('bank-data.csv')
    k=5
    print kmeans(matrix,k)