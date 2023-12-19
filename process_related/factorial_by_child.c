#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<stdlib.h>

int factorial(int n) {
    if (n == 0 || n ==1){
        return 1;
    }else {
        return n*factorial(n-1);
    }
}

int main() {
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    pid_t pid = fork();
    if (pid < 0) {
        perror("Failed to invoke fork() system call\n");
    }else if(pid == 0) {
        int fact = factorial(n);
        printf("This is Child proces, computed factorial\n");
        printf("Factorial of %d is %d\n",n,fact);
        printf("Child process exited\n");
    }else {
        wait(NULL);
        printf("Parent process exited\n");
    }
    return 0;
}