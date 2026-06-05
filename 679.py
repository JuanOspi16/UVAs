from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def main():
    N = int(stdin.readline().strip())

    while N > -1:

        for _ in range(N):
            D, I = map(int, stdin.readline().strip().split())
            nodos = 2 ** D - 1
            ans = busqueda_binaria(I, (nodos+1)//2, nodos)
            print(ans)

        N = int(stdin.readline().strip())

def busqueda_binaria(m, l, h):
    mid = (l+1+h) // 2 
    if m == 1:
        ans = l
    elif m == 2:
        ans = busqueda_binaria(m-1, mid, h)
    else:
        if m % 2 == 1:
            ans = busqueda_binaria(m//2 + 1, l, mid-1)
        else:
            ans = busqueda_binaria(m//2, mid+1, h)
    return ans
    
main()