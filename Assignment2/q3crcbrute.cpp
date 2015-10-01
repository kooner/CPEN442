// Brute force for question 3

#include <iostream>
#include <unordered_map>

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

    std::unordered_map<crc_t, std::string> seen;

    int i = 0;
    while (true) {
        std::string randString = createRandomString(size);
        crc_t crc = getCrc(randString);
        if (seen.count(crc) > 0) {
            std::cout << randString << std::endl;
            auto it = seen.find(crc);
            std::cout << it->second << std::endl;
            break;
        } else {
            seen.insert(std::make_pair(crc, randString));
        }
//        std::cout << i << " " << randString << " " << crc << std::endl;
        i++;
    }

    return 0;
}
