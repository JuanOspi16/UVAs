#include <stdio.h>

int main(){
    int casos;
    int subcasos, a, b;
    scanf("%d", &casos);
    while(casos--){
        int j=0, dif;
        int flag=0;
        scanf("%d", &subcasos);
        while(j<subcasos){

            scanf("%d %d", &a, &b);
            if(j==0){
                dif=a-b;
            }
            if(dif!=a-b && j!=0){
                flag=1;
            }
            j++;
        }
        if(flag==0){
            printf("yes\n");
        }else{
            printf("no\n");
        }
        if(casos) {
            printf("\n");
        }
    }

    return 0;
}