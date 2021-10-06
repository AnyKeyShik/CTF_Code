#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

void
ignore_me_init_buffering(void) 
{
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void
kill_on_timeout(int sig) 
{
  if (sig == SIGALRM) 
  {
  	printf("[!] Anti DoS Signal. Patch me out for testing.");
    _exit(0);
  }
}

void
ignore_me_init_signal(void)
{
	signal(SIGALRM, kill_on_timeout);
	alarm(60);
}

void
WINgardium_leviosa(void) 
{
    printf("┌───────────────────────┐\n");
    printf("│ You are a Slytherin.. │\n");
    printf("└───────────────────────┘\n");
    system("/bin/sh");
}

void
welcome(void)
{
    char read_buf[0xff];
    printf("Enter your witch name:\n");
    gets(read_buf);
    printf("┌───────────────────────┐\n");
    printf("│ You are a Hufflepuff! │\n");
    printf("└───────────────────────┘\n");
    printf(read_buf);
}

void
AAAAAAAA(void)
{
    char read_buf[0xff];
    
    printf(" enter your magic spell:\n");
    gets(read_buf);
    if(strcmp(read_buf, "Expelliarmus") == 0) {
        printf("~ Protego!\n");
    } else {
        printf("-10 Points for Hufflepuff!\n");
        _exit(0);
    }
}

int
main(void)
{
	ignore_me_init_buffering();
	ignore_me_init_signal();

    welcome();
    AAAAAAAA();

    return 0;
}

