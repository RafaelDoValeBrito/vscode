#include <stdio.h>

int main(){

float umidade = 25.0;
float temperatura = 20.0;

if (umidade <= 25.0 && umidade >= 10.0 && temperatura >=10.0 && temperatura <= 20.0)
{
   printf("Clima perfeito");
} 
 else {
    printf("Clima hostil");

}
}