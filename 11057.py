from sys import stdin

def main():
    N = stdin.readline().strip()
    while len(N) > 0:
        N = int(N)
        precios = list(map(int, stdin.readline().strip().split()))
        precios.sort()
        dinero = int(stdin.readline().strip())
        flag = True
        cont = dinero // 2
        ans = -1
        while flag:
            i = busqueda_binaria(precios, cont)
            if i != -1:
                if dinero - cont == cont:
                    if (i + 1 < N and precios[i + 1] == cont) or (i - 1 >= 0 and precios[i - 1] == cont):
                        ans = i
                else:
                    ans = busqueda_binaria(precios, dinero-cont)
                if ans != -1:
                    print(f"Peter should buy books whose prices are {cont} and {precios[ans]}.\n")
                    flag = False
            cont -= 1
        stdin.readline()
        N = stdin.readline().strip()

def busqueda_binaria(precios, dinero):
    low, mid = 0, 0
    high = len(precios) - 1
    ans = -1
    while low <= high and ans == -1:
        mid = (low + high) // 2
        if precios[mid] == dinero:
            ans = mid
        elif precios[mid] < dinero:
            low = mid + 1
        else:
            high = mid - 1
    return ans

main()