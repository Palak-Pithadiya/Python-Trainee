//  Write a C program to demonstrate variables, literal constants,and data types.

#include<stdio.h>

int main() {
    
    // variable
    int a = 10;
    float b = 12.43;
    char c = 'A';

    // Literal constants
    const float PI = 3.14;
    const int MAX = 100;

    printf("a (variable) : %d\n", a);
    printf("b (variable) : %.2f\n", b);
    printf("c (variable) : %c\n", c);
    printf("PI (constant) : %.2f\n", PI);
    printf("MAX (constant) : %d\n", MAX);
    return 0;
}