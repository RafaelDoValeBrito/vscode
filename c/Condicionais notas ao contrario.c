#include <stdio.h>

int main(){

int nota;
    printf("Digite sua nota:\n");
    scanf("%d",&nota);

    if (nota >= 90){
        printf("Sua nota e A!\n");
}   else if (nota >=80 && nota <89){
        printf("Sua nota e B!\n");
}   else if (nota >=70 && nota <79){
        printf("Sua nota e C \n");
}   else if (nota >=60 && nota <69){
        printf("Sua nota E D \n");
}   else if (nota >=50){
        printf("Sua nota E \n");
}    else {
        printf("Sua nota e F \n");


}
}