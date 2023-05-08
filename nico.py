import matplotlib.pyplot as plt
from scipy import stats
import numpy
"""
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
pendiente, intercepción, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
 return pendiente * x + intercepción
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()"""

"""
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline = numpy.linspace(1, 22, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()"""




x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]




from sklearn.cluster import KMeans
datos = list(zip(x, y))
inercias = []
for i in range(1,11):
 kmeans = KMeans(n_clusters=i)
 kmeans.fit(datos)
 inercias.append(kmeans.inertia_)
plt.plot(range(1,11), inercias, marker='o')
plt.title('Método del codo')
plt.xlabel('Número de conglomerados')
plt.ylabel('Inercia')
plt.show()
