#include <stdio.h>

int main(){

int idade;
    printf("Digite sua idade:\n");
    scanf("%d",&idade );
    if (idade > 60){
        printf("Voce e um idoso!\n");
}   else if (idade >=18 && idade <60){
        printf("Voce e um adulto!\n");
}   else if (idade >=12 && idade < 18){
        printf("Voce e adolescente!\n");
}    else {
        printf("Voce e uma crianca");


}
}