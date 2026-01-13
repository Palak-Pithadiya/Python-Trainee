#include<stdio.h>

struct Employee {
    int ID;
    char Name[50];
    int Salary; 
};

int main() {
    int n;
    struct Employee emp[10];
    printf("How many employee data you want to add ? : ");
    scanf("%d", &n);

    for(int i = 0; i < n; i++){
        printf("\nEnter ID: ");
        scanf("%d", &emp[i].ID);

        printf("Enter Name: ");
        scanf("%s", emp[i].Name);

        printf("Enter Salary: ");
        scanf("%d", &emp[i].Salary);
    }

    printf("\nEmployee Details:\n");
    for(int i = 0; i < n; i++) {
        printf("ID : %d, Name : %s, Salary : %d\n",emp[i].ID, emp[i].Name, emp[i].Salary);
    }
    return 0;
}