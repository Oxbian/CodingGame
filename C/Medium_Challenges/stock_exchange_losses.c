#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    int n, v, max = 0, max_lost =0, curr_lost = 0; 
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v);

        curr_lost = v-max;
        if (curr_lost < max_lost) max_lost = curr_lost;
        if (v>max) max = v;
    }
    printf("%d\n",max_lost);

    return 0;
}