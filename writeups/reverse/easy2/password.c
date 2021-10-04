#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "enigma_machine.h"

#define PART_FLAG_LEN 9
#define FLAG_LEN 18
#define PASS_LEN 11

char *ENC_FLAG = "dlbfikqm";
char *ENC_PASS = "dcrtinshzm";

void
generate_flag(char *flag, EnigmaKey *key);

int
main(void)
{
    EnigmaKey *key = calloc(1, sizeof(EnigmaKey));
    char *flag = calloc(FLAG_LEN, sizeof(char));
    char *password = calloc(PASS_LEN, sizeof(char));
    char *user_input = calloc(PASS_LEN, sizeof(char));

    puts("Welcome to super-safety flag store!");
    puts("Try to decrypt flag...");
    puts("-------------------------------------------");

    initEnigmaKey(key);
    generate_flag(flag, key);
    enigma(key, ENC_PASS, password);

    puts("Success!\n");
    printf("Please enter password for see it: ");
    fgets(user_input, PASS_LEN, stdin);

    if (!strcmp(password, user_input)) {
        printf("\nCongrats!\nThats your flag: %s\n", flag);
    } else {
        puts("\nToo bad!");
    }

    free(key);
    free(flag);
    free(password);
    free(user_input);

    return 0;
}

void
generate_flag(char *flag, EnigmaKey *key)
{
    char *flag_part = calloc(PART_FLAG_LEN, sizeof(char));
    
    enigma(key, ENC_FLAG, flag_part);
    strcat(flag, "oren_ctf_");
    strcat(flag, flag_part);
    strcat(flag, "!");

    free(flag_part);
}
