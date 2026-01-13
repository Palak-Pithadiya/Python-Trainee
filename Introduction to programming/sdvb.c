#include <stdio.h>

int main() {
    char s[] = "ABCDEFG";
    int n = 7;

    // First line
    printf("%s\n", s);

    // Remaining lines
    for (int i = 1; i < n - 1; i++) {
        // Left part
        for (int j = 0; j < n - i; j++) {
            printf("%c", s[j]);
        }

        // Spaces
        for (int k = 0; k < (i * 2 - 1); k++) {
            printf(" ");
        }

        // Right part
        for (int j = n - i; j < n; j++) {
            printf("%c", s[j]);
        }

        printf("\n");
    }

    return 0;
}
