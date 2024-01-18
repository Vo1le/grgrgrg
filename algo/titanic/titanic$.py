import pandas
from math import*
import matplotlib.pyplot as plt

titanic=pandas.read_csv("titanic2.csv")
titanic2=pandas.read_csv("titanic3.csv")
titanicverif=pandas.read_csv("titanic.csv")
k = 0

p1="Fare"
p2="Age"
p3="Pclass"
p4="Sexe"
p5="SibSp"
p6="Parch"
puse1=" "
puse2=" "
puse3=" "

x=titanic.loc[:,"Fare"]
y=titanic.loc[:,"Fare"]
z=titanic.loc[:,"Fare"]
lab=titanic.loc[:,"Survived"]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x[lab == 1], y[lab == 1],z[lab == 1], color='g', label='vivant')
ax.scatter(x[lab == 0], y[lab == 0],z[lab == 0], color='r', label='mort')

ax.set_xlabel(puse1)
ax.set_ylabel(puse2)
ax.set_zlabel(puse3)
plt.legend()
plt.show()

def distance (xA,yA,zA,xB,yB,zB): 
    return ((xB-xA)**2+(yB-yA)**2+(zB-zA)**2)**0.5

def knn (dataframe,k,xA,yA,zA):
    dataframe["distance"]= distance(titanic[puse1],titanic[puse2],titanic[puse3],xA,yA,zA)
    dataframe.sort_values(by=['distance'], inplace=True)
    stats0 = 0
    stats1 = 0
    stats= 0
    for i in range(0,k,1):
        if titanic.iloc[i,1] == 0:
            stats0 = stats0 + 1
        elif titanic.iloc[i,1] == 1:
            stats1 = stats1 + 1
    if stats0 > stats1 :
        stats = 0
        return stats
    elif stats1 > stats0:
        stats = 1
        return stats
    else :
        stats = 2
        return stats


def test(k):
    s=0
    result =0
    best = 0
    k = k+ 1
    for t in range(0,len(titanic2),1):
        a = titanic2.iloc[t,9]
        b = titanic2.iloc[t,2]
        c = titanic2.iloc[t,5]
        s = knn(titanic,k,b,a,c)
        if s == titanicverif.iloc[t+594,1]:
            result = result + 1
    result = (result / 298)*100
    print(result , " " , k)
    return result

def ktestor(o):
    m = 0
    y = 1
    res = 0
    bestr = 0
    bestreslt = "rb :"
    for i in range(1,7,1):
        if i < 7:
                puse1 = "p"+str(i)
        for l in range(i+1,7,1):
            if l < 7:
                puse2 = "p"+str(l)
            for p in range(l+1,7,1):
                if p < 7:
                    puse3 = "p"+str(p)
                print(puse1," ",puse2," ",puse3)
                for n in range(0,o,1):
                        res = test(n)
                        if res >= bestr:
                            bestr = res
                            bestreslt = "Best : " + puse1 + " " + puse2 + " " + puse3
                            
        m = m+1
    print(bestreslt)
    print(bestr)

