#include <stdio.h>


int main()
{
    int W,H;
    scanf("%d%d", &W, &H);
    int N;
    scanf("%d", &N);
    int X0,Y0;
    scanf("%d%d", &X0, &Y0);

    int LX = 0, LY = 0, HX = W - 1, HY = H - 1;
    // game loop
    while (1) {
        // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
        char bomb_dir[4];
        scanf("%s", bomb_dir);
        fprintf(stderr,"La bombe est dans la direction: %s",bomb_dir);
        
        if (bomb_dir[0] == 'L' || bomb_dir[1] == 'L')
            HX = X0 - 1;
        else if (bomb_dir[0] == 'R' || bomb_dir[1] == 'R')
            LX = X0 + 1;

        if (bomb_dir[0] == 'U')
            HY = Y0 - 1;
        else
            LY = Y0 + 1;

        X0 = (HX + LX) /2;
        Y0 = (HY + LY) /2;


        // the location of the next window Batman should jump to.
        printf("%d %d\n",X0,Y0);
    }

    return 0;
}