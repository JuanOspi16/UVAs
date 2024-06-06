"""Juan Pablo Ospina
    8972593"""

from sys import stdin

G, visitados = list(), dict()

def main():
    global G, visitados
    casos = int(stdin.readline())
    stdin.readline()
    while casos > 0:
        G, visitados = [], {}
        filas = stdin.readline().strip()
        cont = 0
        while len(filas) != 0:
            G.append(list(filas))
            filas = stdin.readline().strip()
            cont+=1
        print(dfs())
        if casos > 1:
            print()
        casos-=1

def dfs():
    global G, visitados
    mayor = 0
    operacionesX = [1, 0,-1, 0, 1, -1, 1, -1,]
    operacionesy = [0, 1, 0, -1, 1, 1, -1, -1]
    for i in range(len(G)):
        for j in range(len(G[i])):
            cell=0
            if G[i][j] == '1' and (i, j) not in visitados:
                cell = dfsAux(i, j, cell, operacionesX, operacionesy)
                if cell > mayor:
                    mayor = cell
    return mayor

def dfsAux(x, y, cells, opsX, opsY):
    global visitados, G
    if x >= 0 and y >= 0 and x < len(G) and y < len(G[0]) and (x, y) not in visitados and G[x][y] == "1":
        visitados[(x, y)] = 1
        for i in range(len(opsX)):
            cells = dfsAux(x+opsX[i], y+opsY[i], cells, opsX, opsY)
        cells+=1
    return cells

main()