from sys import stdin

def main():
    lineas = int(stdin.readline())
    while lineas != 0:
        n = lineas
        vals=[]
        inversiones = 0
        while n > 0:
            vals.append(int(stdin.readline()))
            n-=1
        tmp = [0]*(len(vals))
        inversiones = mergeSort(vals, 0, len(vals), inversiones, tmp)
        print(inversiones)
        lineas = int(stdin.readline())
    return

def mergeSort(x, low, hi, inversiones, tmp):
    if low+1 < hi:
        mid = low + ((hi-low)>>1)
        inversiones = mergeSort(x, low, mid, inversiones, tmp)
        inversiones = mergeSort(x, mid, hi, inversiones, tmp)
        inversiones = merge(x, low, mid, hi, inversiones, tmp)
    return inversiones

def merge(x, low, mid, hi, inversiones, tmp):
    for i in range(low, hi): tmp[i] = x[i]
    l, r = low, mid
    for n in range(low, hi):
        if l==mid:
            x[n], r = tmp[r], r+1
        elif r==hi:
            x[n], l = tmp[l], l+1
        else:
            if tmp[l]<=tmp[r]:
                x[n], l = tmp[l], l+1
            else:
                x[n], r = tmp[r], r+1
                inversiones += mid - l
    return inversiones
                
main()