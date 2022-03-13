#include <stdio.h>

int main()
{
    // the X position of the light of power
    int light_x;
    // the Y position of the light of power
    int light_y;
    // Thor's starting X position
    int initial_tx;
    // Thor's starting Y position
    int initial_ty;

    scanf("%d%d%d%d", &light_x, &light_y, &initial_tx, &initial_ty);

    // game loop
    while (1) {
        // The remaining amount of turns Thor can move. Do not remove this line.
        int remaining_turns;
        scanf("%d", &remaining_turns);

        char *dirX = "";
        char *dirY = "";

        if ((initial_tx >= 0 && initial_tx < 40) && (initial_ty >= 0 && initial_ty < 18))
        {
            if (initial_tx > light_x)
            {
                dirX = "W";
                initial_tx--;
            }
            else if (initial_tx < light_x)
            {
                dirX = "E";
                initial_tx++;
            }
            else
            {
                dirX = "";
            }

            if (initial_ty > light_y)
            {
                dirY = "N";
                initial_ty--;
            }
            else if (initial_ty < light_y)
            {
                dirY = "S";
                initial_ty++;
            }
            else
            {
                dirY = "";
            }
        }

        
        printf("%s%s\n", dirY, dirX);
    }

    return 0;
}