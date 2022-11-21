#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <fcntl.h>

int pwncollege() { return 0; }

int main(int argc, char* argv[]) {
    // int fd1[2];
    // if (pipe(fd1) == -1) {
    //     return 1;
    // }

    // int fd2[2];
    // if (pipe(fd2) == -1) {
    //     return 1;
    // }

    pid_t pid1 = fork();
    if (pid1 < 0) {
        return 2;
    }

    if (pid1 == 0) {
        // Child process 1 (challenge)
        // dup2(fd1[0], STDIN_FILENO);
        // dup2(fd1[1], STDOUT_FILENO);
        // close(fd1[0]);
        // close(fd1[1]);
        // (fd2[0]);
        // close(fd2[1]);
        // can still view everything
        // dup2(122, 1);
        // char* path = "/tmp/ibscwx";
        // int chdir(const char *path);
        // FILE* fd = fopen("vpipkh", O_RDONLY);
        // dup2(fileno(fd), 1);
        // char line[256];
        // char* envs[] = {"303=hpmdsbsdid", NULL};
        
        // freopen("vpipkh", "r", stdin);
        char* args[] = {NULL};
        int err = execv("/home/hacker/wrap.sh", args);
        if (err == -1) {
            perror("chal");
        }
    }

    // pid_t pid2 = fork();
    // if (pid2 < 0) {
    //     return 3;
    // }

    // if (pid2 == 0) {
    //     // Child process 2 (cat)
    //     dup2(fd1[1], STDOUT_FILENO);
    //     dup2(fd2[0], STDIN_FILENO);
    //     close(fd1[0]);
    //     // close(fd1[1]);
    //     // close(fd2[0]);
    //     close(fd2[1]);
    //     // can still view stderr
    //     int err = execlp("/usr/bin/cat", "cat", NULL);
    //     if (err == -1) {
    //         perror("cat");
    //     }
    // }
    // dup2(fd2[1], STDOUT_FILENO);
    // close(fd1[0]);
    // close(fd1[1]);
    // close(fd2[0]);
    // close(fd2[1]);

    // sleep(1);
    // int err = execlp("/usr/bin/echo", "echo", "cwkqxcyl", NULL);
    // if (err == -1) {
    //     perror("echo");
    // }

    waitpid(pid1, NULL, 0);
    // waitpid(pid2, NULL, 0);

    return 0;
}