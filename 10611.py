from sys import stdin

def main():
    N = int(stdin.readline())
    alturas = list(map(int, stdin.readline().split()))
    Q = int(stdin.readline())
    queries = list(map(int, stdin.readline().split()))
    
    for i in queries:
        baja = buscar_bajo(alturas, i)
        alta = buscar_alto(alturas, i)
        print(replace(baja, -1, alturas), replace(alta, N, alturas))
        
def replace(x, y, alturas):
    if x == y:
        ans = 'X'
    else:
        ans = str(alturas[x])
    return ans

def buscar_alto(alturas, query):
    """
    Busca el indice del número más pequeño que sea mayor que query
    """
    low, high = 0, len(alturas) - 1
    ans = len(alturas)
    while low <= high:
        mid = (low + high) // 2
        if alturas[mid] > query:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def buscar_bajo(alturas, query):
    """
    Busca el índice del número más grande que sea menor que query
    """
    low, high = 0, len(alturas) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if alturas[mid] < query:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

main()