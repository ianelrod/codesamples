#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>

int pwncollege() { return 0; }

struct subprocess {
  pid_t pid;
  int stdin;
  int stdout;
  int stderr;
};

// void *close(int fd) {
//   if (close(fd) == -1) { perror("Could not close pipe end" ); exit(1); }
// }

void mk_pipe(int fds[2]) {
  if (pipe(fds) == -1) { perror("Could not create pipe"); exit(1); }
}

void mv_fd(int fd1, int fd2) {
  if (dup2(fd1,  fd2) == -1) { perror("Could not duplicate pipe end"); exit(1); }
  close(fd1);
}

// Start program at argv[0] with arguments argv.
// Set up new stdin, stdout and stderr.
// Puts references to new process and pipes into `p`.
pid_t call(char* argv[], struct subprocess * p) {
  int child_in[2]; int child_out[2]; int child_err[2];
  mk_pipe(child_in); mk_pipe(child_out); mk_pipe(child_err);
  pid_t pid = fork();
  if (pid == 0) {
    close(0); close(1); close(2);                                 // close parent pipes
    close(child_in[1]); close(child_out[0]); close(child_err[0]); // unused child pipe ends
    mv_fd(child_in[0], 0); mv_fd(child_out[1], 1); mv_fd(child_err[1], 2); // copy new fds to standard locations
    char* envp[] = { NULL };
    // freopen("/home/hacker/cat", "w", stdout);
    execve(argv[0], argv, envp);
  } else {
    close(child_in[0]); close(child_out[1]); close(child_err[1]); // unused child pipe ends
    p->pid = pid;
    p->stdin = child_in[1];   // parent wants to write to subprocess child_in
    p->stdout = child_out[0]; // parent wants to read from subprocess child_out
    p->stderr = child_err[0]; // parent wants to read from subprocess child_err
    return pid;
  }
}

int main(int argc, char* argv[]) {
  alarm(5);
  // char* str1 = "/usr/bin/";
  char* str1 = "/challenge/";
  // char* str1 = "/home/hacker/x.sh";
  // char* str2 = "pwd";
  char* str2 = getenv("CHALLENGE_NAME");
  // char* str3 = "gneipzst\n";
  char buf[4096];
  char* argv[2];
  // argv[0] = str1;
  argv[1] = NULL;

  // strcat(argv[0], env);
  size_t len1 = strlen(str1), len2 = strlen(str2);
  argv[0] = (char*) malloc(len1 + len2 + 1);
  memcpy(argv[0], str1, len1);
  memcpy(argv[0]+len1, str2, len2+1);
  printf("%s\n",argv[0]);

  struct subprocess s;
  call(argv, &s);
  // sleep(1);
  // write(s.stdin,str3,strlen(str3));
  sleep(2);
  int len = read(s.stdout, buf, sizeof(buf) - 1);
  if (len < 0) {
      perror("Read error.");
  } else {
      buf[len] = 0;
      printf("Buffer received: %s\n", buf);
  }
  return 0;
}
