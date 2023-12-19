#include<fcntl.h>
#include<unistd.h>
#include<stdio.h>
int main() {
    int fd = open("example.txt", O_RDWR);
    if (fd == -1) {
        perror("Error opening file");
        return 1;
    }

    write(fd, "Hello, World!", 13);
    lseek(fd, 0, SEEK_SET);

    char buffer[24];
    read(fd, buffer, 13);
    buffer[13] = '\0';
    printf("Content: %s\n", buffer);

    lseek(fd, 0, SEEK_END);
    write(fd, " Appended!", 10);

    lseek(fd, 0, SEEK_SET);
    read(fd, buffer, 23);
    buffer[23] = '\0';
    printf("Updated Content: %s\n", buffer);

    close(fd);
    return 0;
}