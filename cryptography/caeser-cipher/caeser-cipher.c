#include <ctype.h>
// for bool
#include <stdbool.h>
// for isdigit
#include <stdio.h>
// for atoi
#include <stdlib.h>

#define LENGTH 200

bool allDigits(char *str);
void cipher(char *plain, char *cipher, int key);

int main(int argc, char *argv[]) {

  while (argc != 2) {
    printf("Usage: ./ceaser-cipher [ KEY ]\n");
    return 1;
  }

  if (!allDigits(argv[1])) {
    printf("Usage: ./ceaser-cipher [ KEY ]\n");
    return 1;
  }

  char plainText[LENGTH], cipherText[LENGTH];
  int key = atoi(argv[1]);

  printf("Enter the string to cipher:\t");
  scanf("%s", plainText);
  cipher(plainText, cipherText, key);
  printf("The cipherText is: %s \n", cipherText);

  return 0;
}

bool allDigits(char *str) {
  int i = 0;
  while (str[i] != '\0') {
    if (!isdigit(str[i]))
      return false;
    i++;
  };
  return true;
}

void cipher(char *plainText, char *cipherText, int key) {
  int i = 0;
  while (plainText[i] != '\0') {
    char c = plainText[i];
    if (islower(c)) {
      cipherText[i] = 'a' + (c - 'a' + key) % 26;
    } else if (isupper(c)) {
      cipherText[i] = 'A' + (c - 'A' + key) % 26;
    } else {
      cipherText[i] = plainText[i];
    }

    i++;
  }
}
