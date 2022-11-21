#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

int pwncollege() { return 0; }

int main(int argc, char* argv[], char* envp[]) {
    // char* args[317] = {[0 ... 315] = "gixipopmvi", NULL};
    // char* envp[2] = {"228=bfzjqdlpaf", NULL};
    // char* env[] = envp;
    // int fd;
    // char * myfifo = "/tmp/53";
    // mkfifo(myfifo, 0666);
    // freopen("/tmp/qukaae/hydwrd", "r", stdin);

    // char* envs[] = {"303=hpmdsbsdid", NULL};
    char* args[] = {NULL};
    execl("/challenge/embryoio_level101", "/tmp/gqtvcc", NULL);

    return 0;
}