import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
import csv

with open('baseNormalizada.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

#ds = SupervisedDataSet(4, 2)

#ds.addSample((0.9, 0.8, 0.7, 0.9),(0.5 , 0.4))
#ds.addSample((0.29, 0.1, 0.2, 0.9),(0.32 , 0.1))
#ds.addSample((0.4, 0.2, 0.98, 0.2),(0.45 , 0.7))

#print your_list[0]
#print len(your_list[0])

def generateSample(entrada, saida, list):
    print "ds = SupervisedDataSet(" + str(entrada) + "," + str(saida) + ")"
    for i in range(len(list)):
        string1 = ""
        string2 = ""
        for j in range(0,entrada):
            if (j != entrada - 1):
                string1 = string1 + list[i][j] + ","
            elif (j == entrada - 1):
                string1 = string1 + list[i][j]

        for k in range(entrada, entrada + saida):
            if (k < entrada + saida - 1):
                string2 = string2 + list[i][k] + ","
            elif (k == entrada + saida - 1):
                string2 = string2 + list[i][k]

        print "ds.addSample((" + string1 + ")" + ", (" + string2 + "))" + "\n"

generateSample(12,2, your_list)
