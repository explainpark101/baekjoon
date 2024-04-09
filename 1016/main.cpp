#include <stdio.h>
#include <stdint.h>
#include <iostream>
#include <set>



int main() {
    const int64_t maxInt = 1000002;
    int64_t max, min;
    int64_t remainder;
    int64_t forloop_controller;
    int64_t count = 0;
    int64_t i, j;
    int64_t pow_j=0;
    int64_t pow_i=0;
    
    std::cin >> min >> max;
    std::set<int64_t> nums;

    // 정수론 이용해야할 듯? a mod b + c mod b = a+c mod b
    forloop_controller = max - min + 1;
    for(i=3; i<forloop_controller; i+=2) {
        pow_i = i*i;
        remainder = min % pow_i;
        for (j=1;j<forloop_controller; ++j) {
            remainder + (j%pow_i);
        }
    }

    pow_j = 4;
    if(min > pow_j) pow_j = min - (min & 3) + pow_j ;
    while(pow_j <= max) {
        nums.insert(pow_j);
        pow_j += 4;
    }
    for(i=3;i<=maxInt;i+=2) {
        pow_i = i*i;
        if (nums.find(pow_i) != nums.end()) continue;
        if (pow_i > max) break;
        pow_j = pow_i;
        if(min > pow_j) min - (min % pow_j) + pow_j;
        while(pow_j<=max) {
            nums.insert(pow_j);
            pow_j += pow_i;
        }
        std::cout << pow_i << std::endl;
    }

    
    std::cout << max - min + 1 - nums.size();

    return 0;
}