// Review MathsIsFun: Order of Operations. Create a program that demonstrate order of operations to the user. Include parentheses, exponents, multiplication, division, addition, and subtraction in your program. Use variables for the calculations and label the output. For example, part of the program might display: a)1 + 2 * 3 = 7 b)(1 + 2) * 3 = 9

#include <stdio.h>
#include <math.h>

int main() {
    int a = 1, b = 2, c = 3;
    int x = 10, y = 5;

    int r1 = a + b * c;
    int r2 = (a + b) * c;
    float r3 = x / y + 2;
    float r4 = x / (y + 2);
    int r5 = (int)pow(2, 3) + 4;

    printf("a). 1 + 2 * 3 = %d\n", r1);
    printf("b). (1 + 2) * 3 = %d\n", r2);
    printf("c). 10 / 5 + 2 = %.2f\n", r3);
    printf("d). 10 / (5 + 2) = %.2f\n", r4);
    printf("e). 2 ^ 3 + 4 = %d\n", r5);

    return 0;
}
