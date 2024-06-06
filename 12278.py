"""Juan Pablo Ospina Cobo 8972593"""
from sys import stdin
from heapq import heappush, heappop

G, es_estacion = None, None
INF = float('inf')

def main():
    global G, es_estacion
    casos = int(stdin.readline())
    stdin.readline()
    while casos > 0:
        intersecciones = list(map(int, stdin.readline().split()))
        estaciones = list()
        for i in range(intersecciones[0]):
            estacion = int(stdin.readline())
            estaciones.append(estacion-1)
        G = list()  
        G = [[] for _ in range(intersecciones[1])]
        #print(estaciones)
        conexiones = list(map(int, stdin.readline().split()))
        while len(conexiones) != 0:
            conexiones[0] -= 1
            conexiones[1] -= 1
            G[conexiones[0]].append((conexiones[1], conexiones[2]))
            G[conexiones[1]].append((conexiones[0], conexiones[2]))
            conexiones = list(map(int, stdin.readline().split()))
        print(encontrarEstacion(estaciones))
        if casos != 1:
            print()
        casos-=1

"""Se puede retornar la lista ppor cada nodo e ir comparandolo con las distancias del primer dijkstra y sacar el minimo en cada posición y sacar a la vez el maximo de todo el ciclo (el maximo de los minimos) e ir agregando cada 
máximo a una lista en el indice correspondiente"""
"""Después sacar el mínimo de esa lista de máximos y ese sería el nodo"""

def encontrarEstacion(estaciones):
    global G
    minimo = INF
    mejor_estacion = 0
    for j in range(len(G)):
        distancia_casas = dijkstra(estaciones, j)
        maximo = 0
        for i in range(len(G)):
            maximo = max(maximo, distancia_casas[i])
        if maximo < minimo:
            minimo = maximo
            mejor_estacion = j
    mejor_estacion += 1
    return mejor_estacion
    

def dijkstra(estaciones, nodo):
    global G
    dist = [ INF ]*len(G)
    pqueue = list()
    for i in range(len(estaciones)):
        station = estaciones[i]
        dist[station] = 0
        heappush(pqueue, (dist[station], station))
    dist[nodo] = 0
    heappush(pqueue, (dist[nodo], nodo))
    pred = [-1] * len(G)
    while len(pqueue)!=0:
        du,u = heappop(pqueue)
        if dist[u] == du:
            for v,duv in G[u]:
                if du+duv<dist[v]:
                    dist[v] = du+duv
                    pred[v] = u
                    heappush(pqueue, (dist[v], v))
    return dist

main()












