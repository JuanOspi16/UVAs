#include<stdio.h>
#include<malloc.h>
#include<string.h>

int main (){
	char input[10];
    int indice = 1;
	while(scanf("%s", input)){
        if(strcmp(input, "*")==0){
            break;
        }
        else if(strcmp(input, "Hajj") == 0){
            printf("Case %d: Hajj-e-Akbar\n", indice);
        }
        else{
            printf("Case %d: Hajj-e-Asghar\n",indice);
        }
        indice++;
    }
    return 0;
}
