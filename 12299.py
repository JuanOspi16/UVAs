"""Juan Pablo Ospina 8972593"""

from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

A, tree = None, None

def main():
    global A, tree
    caso = list(map(int, stdin.readline().split()))
    A = list(map(int, stdin.readline().split()))
    tree = [0 for _ in range(caso[0]*2)]
    """ print(A) """
    construir(0, 0, caso[0]-1)
    """ print(tree) """
    accion = stdin.readline().strip()
    
    while len(accion) != 0:
        if accion[0] == "q":
            accion = accion[6:-1]
            #print(tree)
            accion = list(map(int, accion.split(",")))
            print(minimo(0, 0, caso[0]-1, accion[0]-1, accion[1]-1))

        elif accion[0] == "s":
            accion = accion[6:-1]
            accion = list(map(int, accion.split(",")))
            aux = A[accion[0]-1]    
            for i in range(len(accion)):
                sgte = (i+1)%len(accion)    
                pos = accion[i]-1
                reemplazo = A[accion[sgte]-1]
                if i == len(accion)-1:
                    reemplazo = aux
                update(0, 0, caso[0]-1, pos, reemplazo)
                A[pos] = reemplazo
        accion = stdin.readline().strip()

def construir(v, l, r):
    global A, tree
    if l == r: tree[v] = A[l]
    else:
        mid = l + ((r-l) >> 1)
        construir(v+1, l, mid)
        construir(v + 2 * (mid - l + 1), mid+1, r)
        tree[v] = min(tree[v+1], tree[v+2*(mid-l+1)]) 

def minimo(v, L, R, l, r):
    global tree
    ans = None
    if l > r: ans = 100001
    elif l == L and r == R: ans = tree[v]
    else:
        mid = L + ((R-L) >> 1)
        ans = min(minimo(v+1, L, mid, l, min(r, mid)), minimo(v+2*(mid - L +1), mid+1, R, max(l, mid + 1), r))
    return ans

def update(v, L, R, pos, h):
    global tree
    if L == R: tree[v] = h
    else:
        mid = L + ((R-L) >> 1)
        if pos <= mid: update(v + 1, L, mid, pos, h)
        else: update(v+2*(mid-L+1), mid+1, R, pos, h)
        tree[v] = min(tree[v+1], tree[v+2*(mid-L+1)])

main()
