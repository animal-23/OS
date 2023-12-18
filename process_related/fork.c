#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<stdlib.h>
int main() {
    pid_t pid = fork();
    printf("Hey there!\n");
    if(pid == 0){
        printf("Child process\n");
    }else if(pid > 0){
        printf("Parent process\n");
    }else {
        perror("Failed to invoke fork() system call");
    }
    return 0;
}