#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<stdlib.h>
int main() {
    pid_t pid = fork();
    if(pid < 0) {
        perror("Failed to invoke fork() system call\n");
    } else if (pid == 0) {
        printf("This is child process, having it's entry in table\n");
    }else {
        printf("This is parent process going to sleep, making it's child ZOMBIE for a moment\n");
        sleep(10);
        printf("Parent process exited retrieving from sleep\n");
    }
    return 0;
}