"""Juan Pablo Ospina"""

from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

G, visitados = list(), dict()

def main():
    global visitados, G
    movimientosX = [-1, 1, 0, 0] 
    movimientosY = [0, 0, -1, 1]
    tamano_matriz = list(map(int, stdin.readline().split()))
    while len(tamano_matriz) != 0:
        visitados={}
        oro = 0
        G = []
        limite = 0
        while limite < tamano_matriz[1]:
            filas = stdin.readline().strip()
            G.append(list(filas))
            for i in range(tamano_matriz[0]):
                if filas[i] == "P":
                    coord = (limite, i)
            limite+=1
        oro = dfs(coord[0], coord[1], oro, movimientosX, movimientosY)
        print(oro)
        tamano_matriz = list(map(int, stdin.readline().split()))
    return 0

def dfs(coordX, coordY, oro, opsX, opsY):
    global visitados, G
    if coordX >= 0 and coordY >= 0 and coordX < len(G) and coordY < len(G[0]) and (coordX, coordY) not in visitados and G[coordX][coordY] != "#" :
        visitados[(coordX, coordY)] = 1
        if  G[coordX +1][coordY] != "T" and G[coordX - 1][coordY] != "T" and G[coordX][coordY +1] != "T" and G[coordX][coordY -1] != "T":
            for i in range(len(opsX)):
                oro = dfs(coordX+opsX[i], coordY+opsY[i], oro, opsX, opsY)
        if G[coordX][coordY] == "G":
            oro+=1
    return oro

main()