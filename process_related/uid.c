#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main() {
    printf("Real User ID is %d\n",getuid());
    printf("Effective User ID is %d\n",geteuid());
    if(setuid(25)!=0){
        perror("setuid() Error!\n");
    }else {
        printf("After setuid() call\n");
        printf("Real User ID is %d\n",getuid());
        printf("Effective User ID is %d\n",geteuid());
    }
    return 0;
}