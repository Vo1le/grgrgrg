import pandas
from math import*
import matplotlib.pyplot as plt

#diabetic=pandas.read_csv("diabetes_data.csv")
diabetic13=pandas.read_csv("diabetes_data13.csv")
diabetic23=pandas.read_csv("diabetes_data23.csv")
s=0
para1 = "bmi"
para2 = "glucose"
para3 = "insulin"

x=diabetic23.loc[:,para1]
y=diabetic23.loc[:,para2]
z=diabetic23.loc[:,para3]
lab=diabetic23.loc[:,"diabetes"]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x[lab == 1], y[lab == 1],z[lab == 1], color='g', label='positif')
ax.scatter(x[lab == 0], y[lab == 0],z[lab == 0], color='r', label='négatif')

def distance (xA,yA,zA,xB,yB,zB): 
    return ((xB-xA)**2+(yB-yA)**2+(zB-zA)**2)**0.5


result = 0

def knn (dataframe,k,xA,yA,zA,t):
    dataframe["distance"]= distance(xA,yA,zA,dataframe[para1],dataframe[para2],dataframe[para3])
    dataframe.sort_values(by=['distance'], inplace=True)
    resultat = 0
    global result
    for i in range(0,k,1):
       if dataframe.iloc[i,8] == 1:
           resultat = 1
       elif dataframe.iloc[i,8] == 0:
           resultat = 0
    if resultat == diabetic13.loc[t,"diabetes"]:
            result = result + 1

def test(k):
    global result
    result = 0
    best = 0
    
    for t in range(0,len(diabetic13)):
        a = diabetic13.loc[t,para1]
        b = diabetic13.loc[t,para2]
        c = diabetic13.loc[t,para3]

        knn(diabetic23,k,a,b,c,t)

    best = (result / 258)*100
    print(best , " " , k)
    return best
for p in range(0,10,1):
    test(p)
