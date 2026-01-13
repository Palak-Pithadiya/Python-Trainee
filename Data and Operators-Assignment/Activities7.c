// Review Wikipedia: Data type. Create a program that demonstrates integer, floating point, and character or string data, and demonstrate converting between data types. For example, user input is always a string, but adding string values of “1” + “1” is typically “11”, whereas, adding numeric values of 1 + 1 is 2. Use variables for the calculations and label the output.

#include <stdio.h>
#include <stdlib.h>  // for atoi

int main() {
    // Integer data
    int intNum1 = 1, intNum2 = 1;
    printf("Integer addition: %d + %d = %d\n", intNum1, intNum2, intNum1 + intNum2);

    // Floating-point data
    float floatNum1 = 1.5, floatNum2 = 2.5;
    printf("Float addition: %.2f + %.2f = %.2f\n", floatNum1, floatNum2, floatNum1 + floatNum2);

    // Character / String data
    char strNum1[] = "1";
    char strNum2[] = "1";
    printf("String concatenation: %s + %s = %s%s\n", strNum1, strNum2, strNum1, strNum2);

    // Converting string to integer
    int converted1 = atoi(strNum1);
    int converted2 = atoi(strNum2);
    printf("String to integer addition: %d + %d = %d\n", converted1, converted2, converted1 + converted2);

    // Converting integer to float
    float convertedFloat = (float)intNum1;
    printf("Integer to float addition: %.2f + %.2f = %.2f\n", convertedFloat, floatNum2, convertedFloat + floatNum2);

    return 0;
}
