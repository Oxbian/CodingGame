#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


int main()
{

    // game loop
    while (1) {
        int mountain_max = 0, mountain_Id = 0;
        for (int i = 0; i < 8; i++) {
            // represents the height of one mountain.
            int mountain_h;
            scanf("%d", &mountain_h);
            if (mountain_h > mountain_max)
            {
                mountain_max = mountain_h;
                mountain_Id = i;
            }
        }
        printf("%d\n",mountain_Id);
    }

    return 0;
}