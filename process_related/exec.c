#include<stdio.h>
#include<unistd.h>
int main() {
    printf("Execution before exec() system call\n");
    execl("/bin/ls","ls","-l",NULL);
    //This stmt will not be executed on successfull exection of exec()
    perror("Execution after exec() system call\n");
    return 0;
}