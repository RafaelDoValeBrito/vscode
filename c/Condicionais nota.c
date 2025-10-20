#include <stdio.h>

int main(){

int nota;
    printf("Digite sua nota:\n");
    scanf("%d",&nota);
    if (nota < 50){
        printf("Sua nota e F!\n");
}   else if (nota >=50 && nota <60){
        printf("Sua nota e D!\n");
}   else if (nota >=60 && nota <70){
        printf("Sua nota e C \n");
}   else if (nota >=70 && nota <80){
        printf("Sua nota E B \n");
}   else if (nota >=90 ){
        printf("Sua nota A+ \n");
}    else {
        printf("Sua nota e A \n");


}
}