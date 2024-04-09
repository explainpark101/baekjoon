#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

int main() {
    const uint64_t maxInt = 1000002;
    uint64_t max, min;
    uint64_t count = 0;
    uint64_t i, j, pow_j;
    int checked;
    scanf("%ld %ld", &min, &max);
    uint64_t* squareArray = (uint64_t*) calloc( maxInt, sizeof(uint64_t) );
    for(i=0;i<maxInt;i++) squareArray[i] = 0;

    for(i=min;i<=max;++i) {
        checked = 1;
        for(j=2;j<maxInt; ++j) {
            if (squareArray[j]) pow_j = squareArray[j];
            else {
                pow_j = (uint64_t) pow((double) j, (double) 2);
                squareArray[j] = pow_j;
            }
            if( pow_j > i) break;
            if (!(i%pow_j)) {
                checked = 0;
                break;
            }
            
        }
        if (checked) ++count;
    }

    printf("%ld", count);

    return 0;
}