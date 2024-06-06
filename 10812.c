#include <stdio.h>
#include<math.h>

int main() {
    int x=0, suma, resta;
    scanf("%d", &x);
    int i=0;
    while(i<x){
        int a, b;
        scanf("%d %d", &a, &b);
        if(a<b){
            printf("impossible\n");
        }
        else{
            resta=(a-b)/2;
            suma=resta+b;
            if(suma+resta==a && abs(suma-resta)==b){
                printf("%d %d\n", suma, resta);
            }else{
                printf("impossible\n");
            }

        }
        i++;
    }
    return 0;
}
