#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<stdlib.h>
int main() {
    pid_t pid = fork();
    printf("Process initiated\n");
    if(pid == 0) {
        printf("This is child process with PID: %d and parent PID: %d\n",getpid(),getppid());
    } else if(pid > 0) {
        printf("This is parent process with PID: %d\n",getpid());
    } else {
        perror("Failed to invoke fork() system call");
    }
    return 0;
}