#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


int main()
{
    int L;
    scanf("%d", &L);
    int H;
    scanf("%d", &H); fgetc(stdin);
    char tab[L][1025];
    char T[257];
    scanf("%[^\n]", T); fgetc(stdin);
    for (int i = 0; i < H; i++) {
        char ROW[1025];
        scanf("%[^\n]", ROW); fgetc(stdin);
        for (int j=0; j<1025; j++)
            tab[i][j] = ROW[j];
    }

    int size=0;
    //On compte la taille du mot
    for (int i =0; i < 257; i++)
    {
        if (T[i] != '\0')
        {
            size++;
            //On convertit notre mot
            if (T[i] > 96 && T[i] < 123)
                T[i] -= 32;
        }
        else
            break;
    }

    //Affichage du mot
    for (int i = 0; i < H; i++) //On répète ça le nombre de lignes
    {
        for (int j = 0; j< size; j++) //Répétition du nombre de lettre pour afficher la ligne i de chaque lettre
        {
            int id = T[j] - 65;
            //fprintf(stderr,"T = %d Id= %d\n",T[j],id);
            if ((id >= 0 && id < 26))
            {
                for (int k =(id*L); k<((id+1)*(L)); k++)
                {
                    printf("%c",tab[i][k]);
                }
            }
            else 
            {
                for (int k =(26*L); k<(27*(L)); k++)
                {
                    printf("%c",tab[i][k]);
                }
            }
        }
        printf("\n");
    }
    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    return 0;
}