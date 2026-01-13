// Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours*rate). Base monthly and annual calculations on 12months per year and 52 weeks per year.
#include<stdio.h>

int main() {

    int hour;
    int rate;
    printf("Enter hours you worked per week : ");
    scanf("%d", &hour);
    printf("Enter rate per hour : ");
    scanf("%d", &rate);

    float weekly_pay = hour*rate;
    float annual_pay = weekly_pay * 52;
    float monthly_pay = annual_pay / 12;

    printf("Weekly pay : %.2f\n", weekly_pay);
    printf("Monthly pay : %.2f\n", monthly_pay);
    printf("Annual pay : %.2f\n", annual_pay);
    
    return 0;
}