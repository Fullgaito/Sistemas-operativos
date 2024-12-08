#include <stdio.h>
int main(int argc,char*argv[]){
    int i;
    printf("Numero de argumentos: ");
    for ( i = 0; i < argc; i++)
    {
        printf("Argumento %d: %s\n",i,argv[i]);
    }
    getchar();
    

    return 0;
}