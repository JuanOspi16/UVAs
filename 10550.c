#include <stdio.h>

int main(){
    int a, b, c, d;
    int suma;
    while(scanf("%d %d %d %d", &a, &b, &c, &d)){

        suma=0;
        if(a==0 && b==0 && c==0 && d==0){
            break;
        }
        else{
            suma=((a+40-b)%40);
            suma+=((40+c-b)%40);
            suma+=((40+c-d)%40);
            suma=(suma+120)*9;
            printf("%d\n", suma);
        }

    }
    return 0;
}