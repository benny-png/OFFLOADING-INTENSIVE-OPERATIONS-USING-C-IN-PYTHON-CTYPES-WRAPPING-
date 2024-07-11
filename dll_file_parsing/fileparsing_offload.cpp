#include <iostream>
#include <fstream>
#include <string>

int parse_csv(const char* filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Could not open file: " << filename << std::endl;
        return -1;
    }

    std::string line;
    while (std::getline(file, line)) {
        // Simple example: print each line
        std::cout << line << std::endl;
    }

    file.close();
    return 0;
}
