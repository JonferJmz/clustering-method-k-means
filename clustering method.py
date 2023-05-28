import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

k = 4 
numData = 10
dimension = 3

def rellenoDatos(k, numData, dimension):
    setData = []
    for i in range(numData):
        datoGen = [random.random() for i in range(dimension)]
        aSumar = random.randint(0, k-1)
        datoGen = [i + aSumar for i in datoGen]
        setData.append(datoGen)
    return setData

def distVect(numData, setData):
    result = 0
    for i in range(numData):
        result1 = setData[i][0]
        result2 = setData[i][1]
        result += (result1 - result2) ** 2
    return math.sqrt(result)

setData = rellenoDatos(k, numData, dimension)

valoresX = [i[0] for i in setData]
valoresY = [i[1] for i in setData]
valoresZ = [i[2] for i in setData]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(valoresX, valoresY, valoresZ, c='b', marker='o')

centroides = []
for _ in range(k):
    centroide = [random.uniform(min(valoresX), max(valoresX)),
                random.uniform(min(valoresY), max(valoresY)),
                random.uniform(min(valoresZ), max(valoresZ))]
    centroides.append(centroide)

centroidX = [i[0] for i in centroides]
centroidY = [i[1] for i in centroides]
centroidZ = [i[2] for i in centroides]

ax.scatter(centroidX, centroidY, centroidZ, c='r', marker='*', s=200, label='Centroids')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

menorDist = []  
closest_centroids = []  

for i, z in enumerate(setData):
    distancias = []
    for j, centroide in enumerate(centroides):
        distancia = math.sqrt(sum([(a - b) ** 2 for a, b in zip(z, centroide)]))
        distancias.append(distancia)
    cercano = min(range(len(distancias)), key=distancias.__getitem__)
    menorDist.append(distancias[cercano])
    print("Distancias", i+1, "- menor distancia:", distancias[cercano])

    cluster_names = ['c1', 'c2', 'c3', 'c4']  
    cluster_asignado = cluster_names[cercano]  
    print("Valor", i+1, "- Cluster asignado:", cluster_asignado)

    ax.text(z[0], z[1], z[2], cluster_asignado)  


for i, centroide in enumerate(centroides):
    ax.text(centroide[0], centroide[1], centroide[2], cluster_names[i])



plt.legend()
plt.tight_layout()
plt.show()
