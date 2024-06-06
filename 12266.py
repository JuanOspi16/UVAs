from sys import stdin
from heapq import heappush, heappop


def main():
    casos = int(stdin.readline())
    while casos>0:
        pedidos = int(stdin.readline())
        compra = []
        venta = []
        acuerdo = 0
        while pedidos>0:
            frase = list(stdin.readline().split())
            acuerdo = orden(frase, compra, venta, acuerdo)
            print("-" if vacio(len(venta)) else venta[0][0], "-" if vacio(len(compra)) else compra[0][0], "-" if vacio(acuerdo) else acuerdo)
            pedidos-=1
        
        casos-=1

def vacio(x):
    return x<=0

def orden(frase, compra, venta, acuerdo): 
    if frase[0] == "buy":
        heappush(compra, [int(frase[4]), int(frase[1])])
        compra.sort(reverse = True)
    else:
        heappush(venta, [int(frase[4]), int(frase[1])])
    while len(venta)!=0 and len(compra)!=0 and venta[0][0] <= compra[0][0]:
        acuerdo = venta[0][0]
        venta[0][1], compra[0][1] = venta[0][1] - compra[0][1], compra[0][1]-venta[0][1]
        if vacio(venta[0][1]):
            heappop(venta)
        if vacio(compra[0][1]):
            heappop(compra)
            compra.sort(reverse = True)
    return acuerdo

main()
