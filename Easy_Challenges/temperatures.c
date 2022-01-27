#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define TAILLE_MAX 10000

int main()
{
    // the number of temperatures to analyse
    int n,min=TAILLE_MAX;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        // a temperature expressed as an integer ranging from -273 to 5526
        int t;
        scanf("%d", &t);

        if (abs((0-t)) < abs(0-min))
        {
            min = t;
        }
        else if (min == t)
        {
            min = t;
        }
        else if (abs(t) == abs(min))
        {
            min = abs(min);
        }
    }

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    if (min == TAILLE_MAX)
        printf("0");
    else
        printf("%d",min);
    return 0;
}