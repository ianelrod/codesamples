#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <regex.h>
#define PORT 1231

int pwncollege() { return 0; }

int main(int argc, char* argv[]) {
    int sock = 0, valread, client_fd;
    struct sockaddr_in serv_addr;
    char buf[2048] = { 0 };
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Socket creation error \n");
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    // Convert IPv4 and IPv6 addresses from text to binary
    // form
    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }

    if ((client_fd = connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr))) < 0) {
        printf("\nConnection Failed \n");
        return -1;
    }

    size_t maxGroups = 2;
    regex_t regex;
    regmatch_t groupArray[maxGroups];
    int value;
    char * regexString = ":\\s(.*)$";
    regcomp(&regex, regexString, REG_EXTENDED);

    // send(sock, hello, strlen(hello), 0);
    // printf("Hello message sent\n");
    unsigned int i = 0;
    for (i = 0; i < 10; i++) {
        int len = read(sock, buf, sizeof(buf) - 1);
        buf[len] = 0;
        printf("%s", buf);
    }

    regexec(&regex, buf, maxGroups, groupArray, 0);
    char sourceCopy[strlen(buf) + 1];
    strcpy(sourceCopy, buf);
    sourceCopy[groupArray[1].rm_eo] = 0;
    char * pro = sourceCopy + groupArray[1].rm_so;
    printf("Problem: %s", pro);
    char str1[16] = "/usr/bin/echo \"";
    char str2[16] = "\" | /usr/bin/bc";
    size_t len1 = strlen(str1), len2 = strlen(pro), len3 = strlen(str2);
    char* com = (char*) malloc(len1 + len2 + len3 + 1);
    memcpy(com, str1, len1);
    memcpy(com+len1, pro, len2);
    memcpy(com+len1+len2, str2, len3+1);
    printf("Command: %s", com);
    FILE *fp = popen(com, "r");
    char res[16];
    fgets(res, sizeof(res), fp);
    pclose(fp);
    printf("Result: %s", res);
    send(sock, res, strlen(res), 0);
    str1[64] = 0;
    str2[64] = 0;
    com = 0;
    res[16] = 0;

    i = 0;
    for (i = 0; i < 2; i++) {
        int len = read(sock, buf, sizeof(buf) - 1);
        buf[len] = 0;
        printf("%s", buf);
    }

    regexec(&regex, buf, maxGroups, groupArray, 0);
    sourceCopy[strlen(buf) + 1];
    strcpy(sourceCopy, buf);
    sourceCopy[groupArray[1].rm_eo] = 0;
    pro = sourceCopy + groupArray[1].rm_so;
    printf("Problem: %s", pro);
    len1 = strlen(str1), len2 = strlen(pro), len3 = strlen(str2);
    com = (char*) malloc(len1 + len2 + len3 + 1);
    memcpy(com, str1, len1);
    memcpy(com+len1, pro, len2);
    memcpy(com+len1+len2, str2, len3+1);
    printf("Command: %s", com);
    fp = popen(com, "r");
    res[16];
    fgets(res, sizeof(res), fp);
    pclose(fp);
    printf("Result: %s", res);
    send(sock, res, strlen(res), 0);
    str1[64] = 0;
    str2[64] = 0;
    com = 0;
    res[16] = 0;

    i = 0;
    for (i = 0; i < 2; i++) {
        int len = read(sock, buf, sizeof(buf) - 1);
        buf[len] = 0;
        printf("%s", buf);
    }

    regexec(&regex, buf, maxGroups, groupArray, 0);
    sourceCopy[strlen(buf) + 1];
    strcpy(sourceCopy, buf);
    sourceCopy[groupArray[1].rm_eo] = 0;
    pro = sourceCopy + groupArray[1].rm_so;
    printf("Problem: %s", pro);
    len1 = strlen(str1), len2 = strlen(pro), len3 = strlen(str2);
    com = (char*) malloc(len1 + len2 + len3 + 1);
    memcpy(com, str1, len1);
    memcpy(com+len1, pro, len2);
    memcpy(com+len1+len2, str2, len3+1);
    printf("Command: %s", com);
    fp = popen(com, "r");
    res[16];
    fgets(res, sizeof(res), fp);
    pclose(fp);
    printf("Result: %s", res);
    send(sock, res, strlen(res), 0);
    str1[64] = 0;
    str2[64] = 0;
    com = 0;
    res[16] = 0;

    i = 0;
    for (i = 0; i < 2; i++) {
        int len = read(sock, buf, sizeof(buf) - 1);
        buf[len] = 0;
        printf("%s", buf);
    }

    regexec(&regex, buf, maxGroups, groupArray, 0);
    sourceCopy[strlen(buf) + 1];
    strcpy(sourceCopy, buf);
    sourceCopy[groupArray[1].rm_eo] = 0;
    pro = sourceCopy + groupArray[1].rm_so;
    printf("Problem: %s", pro);
    len1 = strlen(str1), len2 = strlen(pro), len3 = strlen(str2);
    com = (char*) malloc(len1 + len2 + len3 + 1);
    memcpy(com, str1, len1);
    memcpy(com+len1, pro, len2);
    memcpy(com+len1+len2, str2, len3+1);
    printf("Command: %s", com);
    fp = popen(com, "r");
    res[16];
    fgets(res, sizeof(res), fp);
    pclose(fp);
    printf("Result: %s", res);
    send(sock, res, strlen(res), 0);
    str1[64] = 0;
    str2[64] = 0;
    com = 0;
    res[16] = 0;

    i = 0;
    for (i = 0; i < 2; i++) {
        int len = read(sock, buf, sizeof(buf) - 1);
        buf[len] = 0;
        printf("%s", buf);
    }

    regexec(&regex, buf, maxGroups, groupArray, 0);
    sourceCopy[strlen(buf) + 1];
    strcpy(sourceCopy, buf);
    sourceCopy[groupArray[1].rm_eo] = 0;
    pro = sourceCopy + groupArray[1].rm_so;
    printf("Problem: %s", pro);
    len1 = strlen(str1), len2 = strlen(pro), len3 = strlen(str2);
    com = (char*) malloc(len1 + len2 + len3 + 1);
    memcpy(com, str1, len1);
    memcpy(com+len1, pro, len2);
    memcpy(com+len1+len2, str2, len3+1);
    printf("Command: %s", com);
    fp = popen(com, "r");
    res[16];
    fgets(res, sizeof(res), fp);
    pclose(fp);
    printf("Result: %s", res);
    send(sock, res, strlen(res), 0);
    str1[64] = 0;
    str2[64] = 0;
    com = 0;
    res[16] = 0;

    i = 0;
    for (i = 0; i < 5; i++) {
        int len = read(sock, buf, sizeof(buf) - 1);
        buf[len] = 0;
        printf("%s", buf);
    }

    // closing the connected socket
    close(client_fd);
    return 0;
}