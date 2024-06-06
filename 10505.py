"""
Juan Pablo Ospina Cobo
8972593
"""

from sys import stdin
from collections import deque

G, visitados, invitados, incidencia = None, None, None, None
contador = int()

def main():
    global G, visitados, invitados, incidencia, contador
    casos = int(stdin.readline())
    while casos > 0:
        G, visitados, invitados = list(), list(), dict()
        stdin.readline()
        personas = int(stdin.readline())
        visitados = [False for _ in range(personas)]
        G = [[] for _ in range(personas)]

        for i in range(personas):
            enemigos = list(map(int, stdin.readline().split()))
            for j in range(enemigos[0]):
                G[i].append(enemigos[j+1]-1)
                G[enemigos[j+1]-1].append(i)

        print(bfs())
        casos -=1

def bfs():
    global visitados, invitados
    nodos_solos = 0
    cantidad = 0
    for i in range(len(G)):
        if not visitados[i]:
            if len(G[i]) == 0:
                invitados[i] = 1
                nodos_solos += 1
            else:
                cantidad += bfsAux(i)
    return cantidad + nodos_solos

def bfsAux(v):
    global G, visitados, invitados
    valMax, visitados[v] = True, True
    q = deque()
    q.append(v)
    invitados[v] = 1
    cant_invitados = 1
    cont = 0
    
    while len(q) > 0:
        cont += 1
        v = q.popleft()
        for w in G[v]:
            if not visitados[w]:
                visitados[w] = True
                if v not in invitados:
                    invitados[w] = 1
                    cant_invitados += 1
                q.append(w)
            else:
                if w in invitados and v in invitados:
                    valMax = False
                elif w not in invitados and v not in invitados:
                    valMax = False

    if not valMax:
        cant_invitados = 0
    else: 
        cant_invitados = max(cant_invitados, cont-cant_invitados)
    return cant_invitados


        
main()

