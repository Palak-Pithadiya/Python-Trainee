//Create a program that calculates the area of a room to determine the amount of floor covering required. The room is rectangular with the dimensions measured in feet with decimal fractions. The output needs to be in square yards. There are 3 linear feet (9 square feet) to a yard.

#include<stdio.h>

int main() {

    float l;
    float w;
    printf("Enter Length : ");
    scanf("%d", &l);
    printf("Enter width : ");
    scanf("%d", &w);

    float squ_feet = l * w;
    float yards = squ_feet / 9;

    printf("Square feet : %.2f\n", squ_feet);
    printf("Required floor covering in square yards : %.2f\n", yards);
    
    return 0;
}