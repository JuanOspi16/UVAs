from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

G, visitados, tiempoF, tiempo, pila = None, None, None, None, None

def main():
    global G, pila
    casos = list(map(int, stdin.readline().split()))
    while len(casos) != 0:
        G = list()
        pila = list()
        flag = 0
        G = [[] for _ in range(casos[0])]
        while casos[1] > 0:
            conexiones = list(map(int, stdin.readline().split()))
            if conexiones[0] == 1:
                conexiones[1] -= 1
                conexiones[2] -= 1
                G[conexiones[1]].append(conexiones[2])
            else:
                conexiones[1] -= 1
                for i in range(1, len(conexiones)-1):
                    conexiones[i+1] -= 1
                    G[conexiones[i]].append(conexiones[i+1])
                    G[conexiones[i+1]].append(conexiones[i])
            casos[1]-=1

        dfs(G, range(len(G)), flag)
        flag = 1
        GT = revertir()
        if dfs(GT, pila[::-1], flag):
            print("YES")
        else: print("NO")

        casos = list(map(int, stdin.readline().split()))

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