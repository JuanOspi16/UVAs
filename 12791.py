from math import *
from sys import stdin

def main():
    velocidades = list(map(int, stdin.readline().split()))
    while len(velocidades) != 0:
        vueltas=busquedaBinaria(velocidades)
        print(vueltas)
        velocidades = list(map(int, stdin.readline().split()))
    return 0
        

def busquedaBinaria(vel):
    low, hi = 2, vel[1]+1       
    while hi-low > 1:
        mid=(low+hi)//2
        v=mid*(vel[1] - vel[0])
        if v > vel[1]:
            hi=mid
        else:
            low=mid
    if low * (vel[1] - vel[0]) < vel[1]:
        low=hi
    return low

main()