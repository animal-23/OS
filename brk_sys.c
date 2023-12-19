#include<stdio.h>
#include<unistd.h>
int main() {
    void *new_break = (void *)sbrk(0); // Get the current end of the data segment
    int result = brk(new_break + 4096); // Increase data segment by 4096 bytes

    if (result == 0) {
        printf("brk() successful.\n");
    } else {
        perror("Error in brk()");
    }
    return 0;
}