#include <stdio.h>
#include <stdlib.h>

int parse_csv(const char* filename) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        perror("Could not open file");
        return -1;
    }

    char line[1024];
    while (fgets(line, sizeof(line), file)) {
        // Simple example: print each line
        printf("%s", line);
    }

    fclose(file);
    return 0;
}
