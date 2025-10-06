from sys import stdin

def main():
    master = stdin.readline().strip()
    while master:
        driven = stdin.readline().strip()
        menor = min(len(master), len(driven))
        max_cortes = encajan(driven, master, menor)
        if max_cortes != menor:
            max_cortes = max(encajan(master, driven, menor), max_cortes)
        long = len(master) + len(driven)
        print(long - max_cortes)
        master = stdin.readline().strip()
        

def encajan(driven, master, menor):
    max_cortes = 0
    i = 0
    while i < len(master) and max_cortes != menor:
        a = int(master[i])
        b = int(driven[0])
        if a + b <= 3:
            j, k = 1, i + 1
            contador = 1
            while j < len(driven) and k < len(master) and int(driven[j]) + int(master[k]) <= 3:
                contador += 1
                j += 1
                k += 1
            if j == len(driven) or k == len(master):
                max_cortes = max(max_cortes, contador)
        i += 1
    return max_cortes

main()

