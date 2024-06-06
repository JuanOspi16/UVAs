#include<stdio.h>

int main(){
    int casos=0;
    int n, m, x, y;
    while(scanf("%d", &casos)){
        if(casos == 0){
            break;
        }
        else{
            scanf("%d %d", &n, &m);
            int k=0;
            while(k<casos){
                scanf("%d %d", &x, &y);
                if(x==n || y==m){
                    printf("divisa\n");
                }else if(x<n && y>m){
                    printf("NO\n");
                }
                else if(x<n && y<m){
                    printf("SO\n");
                }
                else if(x>n && y>m){
                    printf("NE\n");
                }
                else if (x>n && y<m){
                    printf("SE\n");
                }
                k++;
            }
        }
    }
    return 0;

}