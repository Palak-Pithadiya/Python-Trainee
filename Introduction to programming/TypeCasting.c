#include<stdio.h>
#include<stdlib.h>

int main(){

    int a = 10;
    float b;

    //Implicit
    b = a;
    printf("Implicit casting:\n");
    printf("int a = %d\n", a);
    printf("float b = %.2f\n\n", b);
 
    char ch = 'A';
    int xo = ch;   

    printf("Character: %c\n", ch);
    printf("Integer(ASCII) : %d\n\n", xo);

    // Explicit 

    float x = 12.75;
    int y;

    y = (int)x;
    printf("Explicit casting:\n");
    printf("float x = %.2f\n", x);
    printf("int y = %d\n\n", y);

    char str[] = "123";
    int num = atoi(str);  

    printf("String: %s\n", str);
    printf("Integer: %d\n", num);

    return 0;
}