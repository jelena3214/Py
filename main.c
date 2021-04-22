#include <stdio.h>
#include <math.h>
#define MAX_SIZE 1000
#define ISPIS(arr, n)\
for (int i = 0; i < n; i++) {\
    printf("%u", arr[i]);\
    if (i < n - 1)putchar(' ');\
}

int main() {
    int n, mask, s, sign, repetition, new_arr[MAX_SIZE];
    int signal[MAX_SIZE] = {0};
    unsigned int temp1, temp2,  arr[MAX_SIZE];

    scanf("%d", &n);
    if (n <= 0 || n > MAX_SIZE) return 0;

    int tmp_unsigned_scanf;

    for (int i = 0; i < n; scanf("%d", &tmp_unsigned_scanf), arr[i++] = tmp_unsigned_scanf);
    ISPIS(arr, n);

    int num = 0;
    for (int i = 0; i < n; i++) {
        mask = 1;
        sign = 1;
        s = 0;
        repetition = log2(arr[i]) + 1;
        if(arr[i] == 0){
            signal[i] = 1, num++;
            continue;
        }
        while (repetition - 1) {
            temp1 = arr[i] & mask;
            temp1 >>= s;
            mask <<= 1;
            s += 1;
            temp2 = arr[i] & mask;
            temp2 >>= s;
            if (temp1 == temp2) {
                sign = 0;
                break;
            }
            repetition--;
        }
        if (sign) signal[i] = 1, num++;
    }
    putchar('\n');

    for (int i = 0; i < n; i++) {
        if (signal[i] == 1) {
            printf("%d", i);
            if (i < n - 1 && num != 1)putchar(' ');
        }
    }

    int new_n, j;
    for (new_n = 0, j = n - 1; j >= 0; j--) {
        if (signal[j])continue;
        new_arr[new_n++] = arr[j];
    }
    putchar('\n');

    ISPIS(new_arr, new_n);
    putchar('\n');

    return 0;
}
