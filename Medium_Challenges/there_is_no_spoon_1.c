#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    // the number of cells on the X axis
    int width;
    scanf("%d", &width);

    // the number of cells on the Y axis
    int height;
    scanf("%d", &height); fgetc(stdin);

    // New grid which will contains all the stuff
    char grid[30][30];
    
    //Getting items from input and adding them into the grid
    for (int i = 0; i < height; i++) {
        char line[32];
        scanf("%[^\n]", line); fgetc(stdin);

        for(int j =0;j < 32; j++){
            grid[i][j] = line[j];
        }
    }

    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            //If we found a node, we print it's coordonnate and after check his neighbours
            if (grid[y][x] == '0')
            {
                printf("%d %d ",x,y);
                short x2, y2, ansX = -1, ansY = -1;
                for (x2 = x+1; x2 < width; ++x2) //Checking if we found another node on the same line
                {
                    if (grid[y][x2] == '0') //If node found we add it as neightbours and stop searching
                    {
                        ansX = x2;
                        ansY = y;
                        break;
                    }
                }
                printf("%d %d ",ansX, ansY);
                ansX = -1; ansY = -1;
                for (y2 = y+1; y2 < height; ++y2) //Checking if we found another node on the same column
                {
                    if (grid[y2][x] == '0') //If we found we add it as neightbours and stop searching
                    {
                        ansX = x;
                        ansY = y2;
                        break;
                    }
                }
                printf("%d %d\n",ansX, ansY);
            }
        }
    }
    return 0;
}
 