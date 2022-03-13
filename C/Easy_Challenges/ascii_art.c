#include <stdio.h>

int main()
{
    //Getting the data
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

    //Counting the size of the word
    for (int i =0; i < 257; i++)
    {
        if (T[i] != '\0')
        {
            size++;
            //Convert the word
            if (T[i] > 96 && T[i] < 123)
                T[i] -= 32;
        }
        else
            break;
    }

    //Printing the word
    for (int i = 0; i < H; i++) //Repeat number of line times
    {
        for (int j = 0; j< size; j++) //Repeat number of letter times
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

    return 0;
}