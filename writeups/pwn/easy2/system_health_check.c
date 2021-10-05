#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

void
ignore_me_init_buffering() 
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
ignore_me_init_signal()
{
	signal(SIGALRM, kill_on_timeout);
	alarm(60);
}

void 
backdoor() 
{
    system("/bin/sh");
}

void
remote_system_health_check() 
{
    char read_buf[0xff];
    puts("Enter password to get system details:\n");
    gets(read_buf);
    if (strcmp(read_buf, "sUp3r_S3cr3T_P4s5w0rD") == 0) {
        puts("Access Granted\n");
        //system("top -b -n 1");
    } else {
        puts("Wrong password!\n");
        _exit(0);
    }
}

int
main(void)
{
	ignore_me_init_buffering();
	ignore_me_init_signal();

    remote_system_health_check();

    return 0;
}

