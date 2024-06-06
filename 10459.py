"""Juan Pablo Ospina Cobo 8972593"""

from sys import stdin
from collections import deque

G, peores_raices, mejores_raices, radio, radio2, visitados = None, None, None, int(), int(), None

def main():
    global G
    casos = stdin.readline()
    while len(casos) != 0:
        casos = int(casos)
        G = list()
        G = [[] for _ in range(casos)]
        for i in range(casos):
            conexiones = list(map(int, stdin.readline().split()))
            conexiones[0] += 1
            for j in range(1, conexiones[0]):
                G[i].append(conexiones[j]-1)
        centro()
        bfs(mejores_raices[0]-1)
        peores_raices.sort()
        print("Best Roots  :", *mejores_raices)
        print("Worst Roots :", *peores_raices )
        casos = stdin.readline()

def centro():
    global peores_raices, G, mejores_raices, radio, radio2
    peores_raices  = list()
    nivelMax = 0
    nivel = [0 for _ in range(len(G))]
    incidencia = [len(G[v]) for v in range(len(G))]
    cola = deque()
    centros = set()
    for i in range(len(G)):
        if incidencia[i] == 1:
            cola.append(i)
    while len(cola) > 0:
        v = cola.popleft()
        for w in G[v]:
            incidencia[w] -= 1
            if incidencia[w] == 1:
                cola.append(w)
                nivel[w] = nivel[v] +1
                nivelMax = max(nivelMax, nivel[w])
    for i in range(len(G)):
        if nivel[i] == nivelMax:
                centros.add(i+1)
    radio = nivelMax
    mejores_raices = list(centros)
    mejores_raices.sort()

def bfs(centro):
    global visitados, radio, radio2, peores_raices
    distancia = [0 for _ in range(len(G))]
    visitados = [False for _ in range(len(G))]
    q = deque()
    visitados[centro] = True
    q.append(centro)
    while len(q) > 0:
        u = q.popleft()
        for v in G[u]:
            if not visitados[v]:
                if len(mejores_raices) == 1 or len(mejores_raices) == 2 and v != mejores_raices[1]-1:
                    distancia[v] = distancia[u] + 1
                if len(G[v]) == 1 and (distancia[v] == radio):
                    peores_raices.append(v+1)
                visitados[v] = True
                q.append(v)

main()