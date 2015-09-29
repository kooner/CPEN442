// Brute force for question 4

#include <iostream>

#include "crc.h"

std::string createRandomString(int size) {
    static const char charset[] =
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    std::string str;
    for (int i = 0; i < size; i++) {
        int key = rand() % (sizeof charset);
        str += charset[key];
    }
    return str;
}

crc_t getCrc(std::string str) {
    crc_t crc = crc_init();
    crc = crc_update(crc, str.c_str(), str.size());
    return crc_finalize(crc);
}

int main(int argc, char* argv[]) {
    int size = 10;
    srand(time(NULL));

    std::string x("8d11b80e3df04178b2827521bd99763b");
    crc_t crcx = getCrc(x);

    int i = 0;
    while (true) {
        std::string randString = createRandomString(size);
        crc_t crc = getCrc(randString);
        if (crc == crcx) {
            std::cout << randString << std::endl;
            break;
        }
        if (i % 10000 == 0) {
            std::cout << i << " " << randString << " " << crc << std::endl;
        }
        i++;
    }

    return 0;
}
