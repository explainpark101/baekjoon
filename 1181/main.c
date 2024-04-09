#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void dswap(char** a, char** b) {
    char* tmp = *b;
    *b = *a;
    *a = tmp;
}
int _strcmp(char* a, char* b){
    int i;
    for(i=0; a[i] && b[i]; i++) {
        if (a==b) continue;
        return a[i] - b[i];
    }
    return 0;
}
int compare(char* a, char* b) {
    int len = strlen(a) - strlen(b);
    if (len) return len;
    len = strcmp(a, b);
    if(!len) a = 0;
    return len;
}

int main() {
    int lineCount;
    int i, j;
    char* strings[20000];
    scanf("%d", &lineCount);
    for(i=0; i<lineCount; i++) {
        strings[i] = (char*) malloc(51 * (sizeof(char*)));
        scanf("%s", strings[i]);

    }

    for(i=0; i<lineCount; i++) {
        for (j=0; j<i; j++) {
            if (i==j) continue;
            if (compare(strings[i], strings[j]) < 0)
                dswap(&strings[i], &strings[j]);
        }
    }

    char* prevString = strings[0];
    printf("%s\n", prevString);
    for(i=1; i<lineCount && strings[i]; i++) {
        if(!strcmp(prevString, strings[i])) continue;
        prevString = strings[i];
        printf("%s\n", prevString);
    }

    return 0;
}