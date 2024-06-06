"""Juan Pablo Ospina Cobo 8972593"""
from sys import stdin
from heapq import heappush, heappop
from collections import deque

INF = float('inf')
G, pred, marcas = None, None, None

def main():
    global G, marcas
    ubicaciones = list(map(int, stdin.readline().split()))
    while len(ubicaciones) != 0:
        G = list()
        G = [[] for _ in range(ubicaciones[0])]
        while ubicaciones[1] > 0:
            conexiones = list(map(int, stdin.readline().split()))
            conexiones[0] -= 1
            conexiones[1] -= 1
            G[conexiones[0]].append((conexiones[1], conexiones[2]))
            G[conexiones[1]].append((conexiones[0], conexiones[2]))
            ubicaciones[1] -= 1
        BH, OF, YH, M = ubicaciones[2]-1, ubicaciones[3]-1, ubicaciones[4]-1, ubicaciones[5]-1
        if BH == YH or BH == M or OF == YH or OF == M:
            print("MISSION IMPOSSIBLE.")
        else:
            distancias = dijkstra1(BH)
            #print(G)
            #print(pred)
            #print(distancias)
            marcarNodos(distancias, OF, BH)
            if not marcas[YH] and not marcas[M]:
                posible = dijkstra2(YH, M)
            else: posible = -1
            if posible == -1:
                print("MISSION IMPOSSIBLE.")
            else:
                print(posible)
        ubicaciones = list(map(int, stdin.readline().split()))

def marcarNodos(distancias, OF, BH):
    global marcas
    marcas = [False for _ in range(len(G))]
    q = deque()
    marcas[OF], marcas[BH] = True, True
    q.append(OF)
    u = INF
    while len(q) != 0:
        u = q.popleft()
        for i, d in G[u]:
            if not marcas[i]:
                x = distancias[i] + d
                if x == distancias[u] and x != INF and i != BH:
                    marcas[i] = True
                    q.append(i)
                

def dijkstra1(s):
    global pred, G
    dist = [ INF ]*len(G) ; dist[s] = 0
    pqueue = list()
    heappush(pqueue, (dist[s], s))
    while len(pqueue)!=0:
        du,u = heappop(pqueue)
        #print(u)
        if dist[u] == du:
            for v,duv in G[u]:
                if du+duv<dist[v]:
                    dist[v] = du+duv
                    heappush(pqueue, (dist[v], v))
    return dist

def dijkstra2(YH, M):
    global marcas, G
    dist = [ INF ]*len(G) ; dist[YH] = 0
    pqueue, found = list(), False
    heappush(pqueue, (dist[YH], YH))
    while len(pqueue)!=0 and not found:
        du,u = heappop(pqueue)
        #print(u)
        if u == M:
            found = True
        else:
            if dist[u] == du:
                for v,duv in G[u]:
                    if du+duv<dist[v]:
                        dist[v] = du+duv
                        if not marcas[v]:
                            heappush(pqueue, (dist[v], v))
    if not found:
        dist[M] = -1
    return dist[M]

main()