#include <stdio.h>
#include <string.h>

int main(){
    char palabras[6][14]={"HELLO", "HOLA", "HALLO", "BONJOUR", "CIAO", "ZDRAVSTVUJTE"};
    char idiomas[6][14]={"ENGLISH", "SPANISH", "GERMAN", "FRENCH", "ITALIAN", "RUSSIAN"};
    char entrada[14];
    int caso=1;
    while(scanf("%s", entrada)){
        if(strcmp(entrada, "#")==0){
            break;
        }else {
            int i = 0;
            while (i < 6){
                if (strcmp(palabras[i], entrada) == 0) {
                    printf("Case %d: %s\n", caso, idiomas[i]);
                    i = 7;
                } else {
                    i++;
                }
            }
            if (i == 6) {
                printf("Case %d: UNKNOWN\n", caso);
            }
            caso++;
        }
    }
    return 0;
}

