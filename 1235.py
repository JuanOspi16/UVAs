"""Juan Pablo Ospina Cobo 8972593"""

from sys import stdin
from heapq import heappush, heappop

G = None
INF = float('inf')


def main():
    global G
    casos = int(stdin.readline())
    while casos > 0:
        conexiones = list(map(str, stdin.readline().split()))
        G = list()
        cantidad = int(conexiones[0])
        G = [[] for _ in range(cantidad+1)]

        for i in range(1, cantidad+1):
            h = calcularPeso("0000", conexiones[i])
            G[0].append((i, h))
            G[i].append((0, h))
            for j in range(i+1, cantidad+1):
                h = calcularPeso(conexiones[i], conexiones[j])
                G[i].append((j, h))
                G[j].append((i, h))
        #print(G)
        print(sumar(prim()))

        casos -= 1

def sumar(arreglo):
    suma_pesos = 0
    for i in range(len(arreglo)):
        suma_pesos += arreglo[i] 
    return suma_pesos

def calcularPeso(inicio, objetivo):
    movimientos = 0
    for i in range(len(inicio)):
        numA = int(inicio[i])
        numB = int(objetivo[i])
        aux = abs(numA - numB)
        if aux > 5:
            aux = 10 - aux
        movimientos += aux
    return movimientos

def prim():
    global G
    visited = [False for _ in range(len(G))]
    c = [ INF ]*len(G) ; c[1] = 0
    p = [-1] * len(G)
    pqueue = list()
    heappush(pqueue, (c[1], 1))
    while len(pqueue)!=0:
        du,u = heappop(pqueue)
        visited[u] = True
        #print(c[u], u)
        if c[u] == du:
            for v,duv in G[u]:
                #print(v)
                if not visited[v] and duv<c[v]:
                    c[v] = duv
                    p[v] = u
                    if v != 0:
                        heappush(pqueue, (c[v], v))
    return c


main()