#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int busqueda_binaria(vector<int> &precios, int dinero, int N);

int main(){
    int N, precio, dinero;
    string str;
    while (scanf("%d", &N) != EOF){
        vector<int> precios;
        for(int i = 0; i < N; i++){
            scanf("%d", &precio);
            precios.push_back(precio);
        }
        scanf("%d", &dinero);
        getline(cin, str);
        getline(cin, str);
        sort(precios.begin(), precios.end());
        bool flag = true;
        int cont = dinero / 2;
        int ans = -1;
        while (flag && cont >= 0){
            int m = busqueda_binaria(precios, cont, N);
            if (m != -1){
                if (dinero - cont == cont){
                    if((m + 1 < N && precios[m + 1] == cont) || (m - 1 >= 0 && precios[m - 1] == cont)){
                        ans = m;
                    }
                }
                else{
                    ans = busqueda_binaria(precios, dinero - cont, N);
                }
                if (ans != -1){
                    printf("Peter should buy books whose prices are %d and %d.\n\n", cont, precios[ans]);
                    flag = false;
                }
            }
            cont--;
        }
    }
    return 0;
}

int busqueda_binaria(vector<int> &precios, int dinero, int N){
    int low = 0, mid = 0;
    int high = N - 1;
    int ans = -1;
    while (low <= high && ans == -1){
        mid = (low + high) / 2;
        if (precios[mid] == dinero){
            ans = mid;
        }
        else if (precios[mid] < dinero){
            low = mid + 1;
        }
        else{
            high = mid - 1;
        }
    }
    return ans;
}