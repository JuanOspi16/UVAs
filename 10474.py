from sys import stdin

def main():
    N, Q = map(int, stdin.readline().split())
    caso = 1

    while N != 0 and Q != 0:
        lista = list()
        for _ in range(N):
            x = int(stdin.readline())
            lista.append(x)
        lista.sort()

        print(f"CASE# {caso}:")

        for _ in range(Q):
            query = int(stdin.readline())
            ans = binary_search(lista, query)
            if ans != -1:
                print(f"{query} found at {ans + 1}")
            else:
                print(f"{query} not found")

        caso += 1
        N, Q = map(int, stdin.readline().split())

def binary_search(lista, query):
    low = 0
    high = len(lista) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == query:
            ans = mid
            high = mid - 1
        elif lista[mid] < query:
            low = mid + 1
        else:
            high = mid - 1

    return ans

#main()
