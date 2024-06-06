"""Juan Pablo Ospina Cobo"""

from sys import stdin
from fractions import Fraction

G, items, code, visitados = list(), list(), dict(), list()

def main():
    global G, items, code, visitados
    comando = stdin.readline()
    while len(comando)!=2:
        tok=comando.split()
        if tok[0][0]=='!':
            v0, c0, v1, c1 = int(tok[1]), encode(tok[2]), int (tok[4]), encode(tok[5])
            G[c0].append((c1, Fraction(v1, v0)))
            G[c1].append((c0, Fraction(v0, v1)))
        else:
            c0, c1 = encode(tok[1]), encode(tok[3])
            equivalencia = dfs(c0, c1)
            print("{} {} = {} {}".format(equivalencia[0], tok[1], equivalencia[1], tok[3]))
        comando = stdin.readline() 
    return 0

def dfs(c0, c1):
    num, dem = 1, 1
    global visitados
    visitados = [False for _ in range(len(G))]
    num, dem = dfsAux(c0, num, dem, c1)
    if not visitados[c1]:
        valor = ["?", "?"]
    else:
        a = Fraction(dem, num)
        valor = [a.numerator, a.denominator]
    return valor

def dfsAux(u, num, dem, c1):
    global visitados
    visitados[u] = True
    for v in G[u]:
        if not visitados[v[0]] and not visitados[c1]:
            num, dem = dfsAux(v[0], num, dem, c1)
            if visitados[c1]:
                num *= v[1].numerator
                dem *= v[1].denominator
    return num, dem

def encode(item):
    global items, code
    if item not in code:
        code[item] = len(code)
        G.append(list())
        items.append(item)
    return code[item]

main()