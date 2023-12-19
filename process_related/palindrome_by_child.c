#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<stdlib.h>
#include<stdbool.h>

int palindrome(int n) {
    int temp = n;
    int temp1 = 0;
    int temp2;
    while (temp) {
        temp2 = temp%10;
        temp1 = temp1*10+temp2;
        temp = temp/10;
    }
    return (temp1 == n);
}

int main() {
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    pid_t pid = fork();
    if (pid < 0) {
        perror("Failed to invoke fork() system call\n");
        exit(1);
    }else if(pid == 0) {
        bool status = palindrome(n);
        printf("This is child process, computed palindorme\n");
        if (status) {
            printf("%d is a palindrome number\n",n);
        }else {
            printf("%d is not a palindrome\n",n);
        }
        printf("Child process exited\n");
    }else {
        wait(NULL);
        printf("Parent process exited\n");
    }
    return 0;
}