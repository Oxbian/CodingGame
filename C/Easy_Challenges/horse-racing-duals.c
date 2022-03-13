#include <stdlib.h>
#include <stdio.h>

int compare (const void *arg1, const void *arg2) {
   return (*(int*)arg1 - *(int*)arg2);
}

int main()
{
    int N, diff = 2147483647;
    scanf("%d", &N);
    int tab[N];
    for (int i = 0; i < N; i++)
        scanf("%d", &tab[i]);

    qsort (tab,N,sizeof(int),compare);
    for (int i =0; i<N; i++)
    {
        if (abs(tab[i] - tab[i+1]) < diff)
            diff = abs(tab[i] - tab[i+1]);
    }
    printf("%d\n",diff);

    return 0;
}