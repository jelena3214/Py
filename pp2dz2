#include <stdio.h>
#include <stdlib.h>

void safe_allocate2(char **temp){
    if(temp == NULL){
        printf("MEM_GRESKA");
        exit(0);
    }
}
void safe_allocate(char *temp){
    if(temp == NULL){
        printf("MEM_GRESKA");
        exit(0);
    }
}
int min_arr(int *arr, int n){
    int temp = arr[0];
    for(int i = 1; i < n; i++){
        if(temp > arr[i])temp = arr[i];
    }
    return temp;
}

int main() {
    int n, m, temp;
    scanf("%d %d", &n, &m);
    char **matrix;
    matrix = malloc(n*sizeof(char*));
    safe_allocate2(matrix);
    for(int i = 0; i < n; i++){
        matrix[i] = malloc(m*sizeof(char ));
        safe_allocate(matrix[i]);
    }

    //unos

    for(int i = 0; i < n; i++){
        int j = 0;
        while(j < m){
            temp = getchar();
            if(temp != ' ' && temp != '\n'){
                matrix[i][j++] = temp;
            }
        }
    }

    //ispis
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            printf("%c", matrix[i][j]);
            if(j != m -1)putchar(' ');
        }
        putchar('\n');
    }
    int min_horizontal, arr[n], tp , flag;
    for(int i = 0; i < n; i++){
        int pom = 0;
        flag = 0;
        tp = 1000;
        for(int j = 0; j < m; j++){
            if(matrix[i][j] == '*' && j != m-1){
                if(pom < tp && flag)tp = pom;
                pom = 0;
                flag = 0;
                continue;
            }
            if(matrix[i][j] != '*')pom++;
            if(j == m-1 && tp == 1000)tp = pom;
            flag = (j != n - 1)?1:0;
        }
        if(pom < tp && flag)tp = pom;
        arr[i] = tp;
    }
    min_horizontal = min_arr(arr, n);
    //printf("%d\n", min_horizontal);


    int min_vertical, arr1[m];
    for(int i = 0; i < m; i++){
        int pom = 0;
        flag = 0;
        tp = 1000;
        for(int j = 0; j < n; j++){
            if(matrix[j][i] == '*' && j != n-1){
                if(pom < tp && flag)tp = pom;
                pom = 0;
                flag = 0;
                continue;
            }
            if(matrix[j][i] != '*')pom++;
            if(j == n-1 && tp == 1000) tp = pom;
            flag = (j != n - 1)?1:0;
        }
        if(pom < tp && flag)tp = pom;
        arr1[i] = tp;
    }
    min_vertical = min_arr(arr1, m);
    printf("%d %d\n", min_horizontal, min_vertical);


    printf("VODORAVNO\n");

    int lenth = 0, row, col, cord[2*n], notin = 1, k = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(matrix[i][j] != '*'){
                lenth++;
                if(notin) {
                    row = i;
                    col = j;
                    notin = 0;
                }
            }
            if((matrix[i][j] == '*' || j == m-1) && lenth == min_horizontal){
                cord[2*k] = row;
                cord[2*k+1] = col;
                k++;
                notin = 0;
                lenth = 0;
            }
            if(matrix[i][j] == '*')lenth = 0, notin = 1;
        }
        lenth = 0;
        notin = 1;
    }
    char *niz = calloc(min_horizontal+1, sizeof(char));
    for(int i = 0; i < k; i++) {
        for (int j = 0; j < min_horizontal; j++) {
            niz[j] = matrix[cord[2 * i]][cord[2 * i + 1] + j];
        }
        printf("(%d, %d, %s)", cord[2*i], cord[2*i + 1], niz);
        putchar('\n');
    }
    free(niz);
    printf("USPRAVNO\n");

    int cord1[2*m];
    notin = 1;
    k = 0;
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(matrix[j][i] != '*'){
                lenth++;
                if(notin) {
                    row = i;
                    col = j;
                    notin = 0;
                }
            }
            if((matrix[j][i] == '*' || j == n-1) && lenth == min_vertical){
                cord1[2*k] = col;
                cord1[2*k+1] = row;
                k++;
                notin = 0;
                lenth = 0;
            }
            if(matrix[j][i] == '*')lenth = 0, notin = 1;
        }
        lenth = 0;
        notin = 1;
    }
    for(int i = 0; i < k - 1; i++){
        if(cord1[2*i] > cord1[2*i+2]){
            int tmp = cord1[2*i];
            cord1[2*i] = cord1[2*i+2];
            cord1[2*i+2] = tmp;
            int tmp1 = cord1[2*i+1];
            cord1[2*i+1] = cord1[2*i+3];
            cord1[2*i+3] = tmp1;
        }
    }

    niz = calloc(min_vertical+1, sizeof(char));
    for(int i = 0; i < k; i++) {
        for (int j = 0; j < min_vertical; j++) {
            niz[j] = matrix[cord1[2 * i] + j][cord1[2 * i + 1]];
        }
        printf("(%d, %d, %s)", cord1[2*i], cord1[2*i + 1], niz);
        putchar('\n');
    }
    free(niz);
    for(int i = 0; i < n; i++){
        free(matrix[i]);
    }
    free(matrix);

    return 0;
}
