#include <stdio.h>

int 
main(void) 
{
    setvbuf(stdout, NULL, _IONBF, 0);
    
    puts("Give me A and B and I'll give you A/B");
    puts("If you crush me, my master give you flag");
    
    int a = 0, b = 0;
    
    if (scanf("%d%d", &a, &b) != 2) {
        puts("Liar!! This is'not two numbers!!!");
        return 0;
    }
    if (b == 0) {
        puts("Not so easy");
        return 0;
    }

    printf("A: %d, B: %d, A / B: %d\n", a, b, a / b);
    
    return 0;
}

