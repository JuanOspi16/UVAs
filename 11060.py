"""Juan Pablo Ospina"""

from sys import stdin

code, G, topo, visited = dict(), list(), list(), list()

def main():
    global G, code, topo, visited
    cantBebida = stdin.readline()
    caso = 1
    while cantBebida != '':
        cantBebida = int(cantBebida)
        code, G, topo, visited = {}, [], [], [0 for _ in range(cantBebida)]
        gradoIncidencia=[0 for _ in range(cantBebida)]
        bebidas = []
        cont=0
        while cont < cantBebida:
            beb = stdin.readline().split()
            G.append(list())
            bebidas.append(beb[0])
            code[beb[0]] = cont
            cont += 1
        orden = int(stdin.readline())
        while orden > 0:
            alcohol = stdin.readline().split()
            G[code[alcohol[0]]].append(code[alcohol[1]])
            gradoIncidencia[code[alcohol[1]]]+=1
            orden-=1
        orden_topologico(0, gradoIncidencia, bebidas)
        print("Case #{}: Dilbert should drink beverages in this order: {}.\n".format(caso, ' '.join(topo)))
        stdin.readline()
        cantBebida = stdin.readline()
        caso +=1
        

def orden_topologico(p, inc, bebidas):
    global G, topo, visited, code
    if p < len(G):
        r, i = -1, 0
        while i < len(G) and r == -1:
            if visited[i] == 0 and inc[i] == 0: r = i
            i += 1
        if r != -1:
            for v in G[r]:
                inc[v] -= 1
            visited[r] = 1
            topo.append(bebidas[r])
            orden_topologico(p + 1, inc, bebidas)

main()