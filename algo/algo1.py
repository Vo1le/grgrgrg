import pandas
from math import*
import matplotlib.pyplot as plt
a = float(input("La largeur du pétale :"))
b = float(input("La longueur du pétale :"))
k = int(input("Nombre de voisins :"))
iris=pandas.read_csv("iris.csv")
x=iris.loc[:,"petal_length"]
y=iris.loc[:,"petal_width"]
lab=iris.loc[:,"species"]
plt.axis('equal')
plt.scatter(x[lab == 0], y[lab == 0], color='g', label='setosa')
plt.scatter(x[lab == 1], y[lab == 1], color='r', label='versicolor')
plt.scatter(x[lab == 2], y[lab == 2], color='b', label='virginica')
plt.scatter(b, a, color='k')

r = 0

liste=[]

def distance (xA,yA,xB,yB): 
    return ((xB-xA)**2+(yB-yA)**2)**0.5

def knn (dataframe,k,xA,yA):
    dataframe["distance"]= distance(iris["petal_length"],iris["petal_width"],xA,yA)
    dataframe.sort_values(by=['distance'], inplace=True)
    stats0 = 0
    stats1 = 0
    stats2 = 0
    for i in range(0,k,1):
        if iris.iloc[i,2] == 0:
            stats0 = stats0 + 1
        elif iris.iloc[i,2] == 1:
            stats1 = stats1 + 1
        else :
            stats2 = stats2 + 1
    if stats0 > stats1 and stats0 > stats2:
        print("Votre espéce est l'iris setosa")
    elif stats1 > stats0 and stats1 > stats2:
        print("Votre espéce est l'iris versicolor")
    elif stats2 > stats1 and stats2 > stats0:
        print("Votre espéce est l'iris verginica")
    else :
        print("Pas de résultat précis")
    
knn(iris,k,b,a)
plt.legend()
plt.show()
