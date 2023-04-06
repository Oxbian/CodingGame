#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Convert char into binary ascii
void charToBin(char c, char *buffer)
{
    for (int i = 6; i >=0; i--)
    {
        buffer[i] = '0' + c%2;
        c/=2;
    }
    buffer[7] = '\n';
}

int main()
{
    char MESSAGE[101], binary[8], binMessage[707], prev;
    int i = 0, j = 0, count = 0;
    scanf("%[^\n]", MESSAGE);
    binMessage[0] = '\0'; //Reset the string

    for (int i = 0; i < strlen(MESSAGE); i++)
    {
        charToBin(MESSAGE[i], binary);
        strncat(binMessage,binary,7); //Adding the binary of each char into the binMessage string
    }

    for (i =0; binMessage[i] != '\0'; i++)
    {
        if (binMessage[i] != prev)
        {
            for (j=0; j<count; j++)
                printf("0");

            if (count != 0)
                printf(" ");

            printf((binMessage[i] == '0') ? "00 " : "0 ");
            count =1;
        }
        else
            count++;

        prev = binMessage[i];
    }
    for (int j = 0 ; j < count ; j++) //Showing the rest of the binMessage string
        printf("0");     
    return 0;
}  