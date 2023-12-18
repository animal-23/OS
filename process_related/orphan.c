#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<stdlib.h>
int main() {
    pid_t pid = fork();
    if (pid < 0) {
        perror("Failed to invoke fork() system call\n");
    }else if(pid == 0) {
        printf("This is child process going to ORPHAN state\n");
        sleep(10);
        printf("Child process retieved from ORPHAN state, adopted by Kernel\n");
    }else {
        printf("This is parent process exiting as soon as invoked");
    }
    return 0;
}