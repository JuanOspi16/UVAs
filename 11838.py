from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

G, visitados, tiempoF, tiempo, pila = None, None, None, None, None

def main():
    global G, pila
    intersecciones_calles = list(map(int, stdin.readline().split()))
    while intersecciones_calles[0] != 0 and intersecciones_calles[1] != 0:
        calles = intersecciones_calles[1]
        G = list()
        pila = list()
        flag = 0
        G = [[] for _ in range(intersecciones_calles[0])]
        while calles > 0:
            nodos = list(map(int, stdin.readline().split()))
            G[nodos[0]-1].append(nodos[1]-1)
            if nodos[2] == 2:
                G[nodos[1]-1].append(nodos[0]-1)
            calles-=1

        dfs(G, range(len(G)), flag)
        flag = 1
        GT = revertir()
        if dfs(GT, pila[::-1], flag):
            print(1)
        else: print(0)

        intersecciones_calles = list(map(int, stdin.readline().split()))

def revertir():
    global G
    ans = [list() for _ in G]
    for u in range(len(G)):
        for v in G[u]:
            ans[v].append(u)
    return ans

def dfs(G, orden, flag):
    global visitados, tiempoF, tiempo
    ans = list()
    visitados, tiempoF, tiempo = list(), list(), 0
    for _ in G:
        visitados.append(0)
        tiempoF.append(None)
    for u in orden:
        if visitados[u] == 0:
            ans.append(list())
            dfsAux(G, u, ans[-1], flag)
    return len(ans) == 1

def dfsAux(G, u, comp, flag): 
    global visitados, pila, tiempoF, tiempo
    visitados[u], tiempo = 1, tiempo+1
    comp.append(u)
    for v in G[u]:
        if visitados[v] == 0:
            dfsAux(G, v, comp, flag)
    tiempoF[u], tiempo = tiempo, tiempo+1
    if flag == 0:
        pila.append(u)

main()
