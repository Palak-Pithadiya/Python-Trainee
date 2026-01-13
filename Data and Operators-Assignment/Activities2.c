// Create a program that asks the user how old they are in years, and then calculate and display their approximate age in months, days, hours, and seconds For example, apers on 1 year old is 12 months old, 365 days old, etc.

#include<stdio.h>

int main() {

    int age;
    printf("Enter age in year : ");
    scanf("%d", &age);

    int months = age * 12;
    int days = age * 365;
    int hours = days * 24;
    int seconds = hours * 3600;

    printf("approximate age in months : %d\n", months);
    printf("approximate age in days : %d\n", days);
    printf("approximate age in hours : %d\n", hours);
    printf("approximate age in seconds : %d\n", seconds);
    
    return 0;
}