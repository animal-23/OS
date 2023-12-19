#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Original nice value: %d\n", nice(0));

    int increment = 10;
    int new_nice = nice(increment);

    if (new_nice == -1) {
        perror("Error changing nice value");
    } else {
        printf("Nice value after incrementing by %d: %d\n", increment, new_nice);
    }

    return 0;
}
