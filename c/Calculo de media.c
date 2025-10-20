#include <stdio.h>

int main(){

    int idade, matricula;
    float altura;
    char nome[50];

    printf("Digite sua idade:  \n");
    scanf("%d", &idade);

    printf("Digite sua altura:  \n");
    scanf("%f", &altura);

    printf("Digite o seu nome: \n");
    scanf("%s", &nome);

    printf("Digite matricula: \n");
    scanf("%d", &matricula);

    printf("Idade: %d \n", idade);
    printf("Altura: %f\n", altura);
    printf("Nome do Aluno: %s \n", nome);
    printf("Matricula: %d \n", matricula);
    
    

    return 0;



}