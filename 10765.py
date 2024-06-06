from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)


G, visitados, low, padres, numHijos= None, None, None, None, None
puntos_articulacion = dict()
t, n = int(), int()

def main():
    global  G, visitados, low, padres, numHijos, puntos_articulacion, t, n

    casos = list(map(int, stdin.readline().split()))
    while casos[0] != 0 and casos[1] != 0:
        G=[[] for _ in range(casos[0])]
        visitados, low, padres, numHijos = list(), list(), list(), list()
        puntos_articulacion = dict()
        t, n = 0, casos[0]
        puntos_componentes = list()

        nodos = list(map(int, stdin.readline().split()))
        while nodos[0] != -1 and nodos[1] != -1:
            G[nodos[0]].append(nodos[1])
            G[nodos[1]].append(nodos[0])
            nodos = list(map(int, stdin.readline().split()))
            
        ap()
        ordenar(casos[1], puntos_componentes)
        print()
        casos = list(map(int, stdin.readline().split()))
    return 0

def ordenar(objetivos, puntos):
    global puntos_articulacion, numHijos
    for i in puntos_articulacion:
       puntos.append((i, puntos_articulacion[i]))
    puntos.sort(key=lambda x:(-x[1], x[0]))
    j, k, i = 0, 0, 0 # j para recorrer los pa, k para recorrer el grafo, e i para parar cuando se terminen las bombas
    while j < len(puntos) and j < objetivos:
        print(puntos[j][0], puntos[j][1])
        j+=1
    if len(puntos) < objetivos:
        while k < len(G) and i < objetivos-j:
            if k not in puntos_articulacion:
                print(k, 1)
                i+=1
            k+=1        
        

def ap():
    global low, visitados, padres, n, numHijos

    low = [-1 for _ in range(n)]
    visitados = [-1 for _ in range(n)]
    padres = [-1 for _ in range(n)]
    numHijos = [0 for _ in range(n)]
    
    for i in range(n):
        if visitados[i] == -1:
            apAux(i)

def apAux(v):
    global low, visitados, padres, puntos_articulacion, t, G
    t += 1
    visitados[v] = low[v] = t

    for w in G[v]:
        if visitados[w] == -1:
            padres[w] = v
            numHijos[v] +=1
            apAux(w)
            low[v] = min(low[v], low[w])

            if padres[v] != -1 and low[w] >= visitados[v]:
                if v not in puntos_articulacion:
                    puntos_articulacion[v] = 2 #2: 1 del componente de ancestros, 1 del hijo
                else:
                    puntos_articulacion[v] +=1

        elif w != padres[v]:
            low[v] = min(low[v], visitados[w])

    if padres[v] == -1 and numHijos[v] > 1:
        if v not in puntos_articulacion:
            puntos_articulacion[v] = numHijos[v] 
        

main()