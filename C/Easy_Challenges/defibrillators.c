#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

double distance (double latA, double longA, double latB, double longB)
{
    fprintf(stderr, "Affichage des valeurs de latA %lf et longA %lf, latB %lf et longB %lf\n",latA, longA, latB, longB);
    return (sqrt(pow((longB-longA)*cos((latA + latB)/2),2)+pow((latB - latA),2)) * 6371);
}

char *floatFrToUs(const char *textToTransform)
{
    char *token[3] = {NULL};
    int counter = 0;
    char *next_token = strtok(textToTransform, ",");
    while(next_token != NULL ) 
    {
        size_t token_length = strlen(next_token);
        token[counter] = calloc(token_length, sizeof(char));
        memcpy(token[counter], next_token, token_length);
        next_token = strtok(NULL, ",");
        ++counter;
    }
    char *result = malloc(strlen(token[0]) + strlen(token[1]) + strlen(".") + 1);
    memcpy(result, token[0], strlen(token[0])); 
    memcpy(result + strlen(token[0]), ".", strlen(".") + 1);
    memcpy(result + strlen(token[0]) + strlen("."), token[1], strlen(token[1]) + 1);
    return result;
}

int main()
{
    char LON[51], LAT[51], result[257];
    scanf("%s%s", LON, LAT);
    fprintf(stderr,"Debug LON: %s, LAT: %s\n",LON,LAT);
    double lon = 0, lat = 0;
    sscanf(floatFrToUs(LON), "%lf", &lon);
    sscanf(floatFrToUs(LAT), "%lf", &lat);
    fprintf(stderr,"Debug LON: %s, LAT: %s\n",LON,LAT);

    int N, counter = 0;
    float min = 99999999;
    scanf("%d", &N); fgetc(stdin);
    for (int i = 0; i < N; i++) {
        char DEFIB[257], *token[8] = {NULL};
        scanf("%[^\n]", DEFIB); fgetc(stdin);
        char *next_token = strtok(DEFIB, ";");
        while(next_token != NULL ) 
        {
            size_t token_length = strlen(next_token);
            token[counter] = calloc(token_length, sizeof(char));
            memcpy(token[counter], next_token, token_length);
            next_token = strtok(NULL, ";");
            ++counter;
        }
        for (int j =0; j<counter; j++)
            fprintf(stderr,"%d: %s\n",i,token[j]);

        double dist = 0, entryLon = 0, entryLat = 0;
        sscanf(floatFrToUs(token[counter-2]), "%lf", &entryLon);
        sscanf(floatFrToUs(token[counter-1]), "%lf", &entryLat);
        dist = distance(lat, lon, entryLat, entryLon);
        fprintf(stderr, "Affichage des valeurs de lon %.4lf et lat %.4lf\n",entryLon, entryLat);
        fprintf(stderr,"Valeur distance: %f\n",dist);
        if (dist < min)
        {
            fprintf(stderr,"Valeur copier car dist vaut %lf\n",dist);
            min = dist;
            strcpy(result,token[1]);
        }
        counter = 0;
    }

    printf("%s\n",result);

    return 0;
}