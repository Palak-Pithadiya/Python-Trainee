// Review MathsIsFun : US Standard Lengths. Create a program that asks the  user for adistance in miles and then calculate and display the distance in yards, feet, and inches, or ask the user for adistance in miles and then calculate and display the distance in kilometers, meters, and centimeters.


#include<stdio.h>

int main() {

    float miles;
    printf("Enter distance in miles : ");
    scanf("%f", &miles);

    float km = miles * 1.609; 
    float m = km * 1000;
    float cm = m * 100;
    
    printf("Distance in KiloMeter : %.2f\n", km);
    printf("Distance in Meter : %.2f\n", m);
    printf("Distance in CentiMeter : %.2f\n", cm);

    return 0;
}