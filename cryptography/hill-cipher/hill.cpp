// assuming that key is only of capital letters
#include <iostream>

using namespace std;

void getKeyMatrix(string key, int keyMatrix[][3]) {
  int index = 0;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      keyMatrix[i][j] = (key[index]) % 65;
      index++;
    }
  }
}

// this function encrypts each message *block*
void encrypt(int cipherMatrix[][1], int keyMatrix[][3],
             int messageVector[][1]) {
  // for each element of messageVector, calculate element of cipherMatrix
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 1; j++) {
      cipherMatrix[i][j] = 0;
      // to calculate (i, j) of cipherMatrix, each (i, x) element of keyMatrix
      // must be multiplied with messageVector's (x, j) element and the results
      // should be added (do in copy)
      for (int x = 0; x < 3; x++) {
        cipherMatrix[i][j] += keyMatrix[i][x] * messageVector[x][j];
      }
      cipherMatrix[i][j] = cipherMatrix[i][j] % 26;
    }
  }
}

void hillCipher(string message, string key) {
  int keyMatrix[3][3];
  getKeyMatrix(key, keyMatrix);

  int messageVector[3][1];

  for (int i = 0; i < 3; i++)
    messageVector[i][0] = (message[i]) % 65;

  int cipherVector[3][1];
  encrypt(cipherVector, keyMatrix, messageVector);

  string cipherText;

  // Generate the encrypted text from 
  // the encrypted vector
  for (int i = 0; i < 3; i++)
      cipherText += cipherVector[i][0] + 65;
 
  // Finally print the ciphertext
  cout << " Ciphertext:" << cipherText;
}

int main() {
  // Get the message to be encrypted
  string message = "ACT";

  // Get the key
  string key = "GYBNQKURP";

  hillCipher(message, key);

  return 0;
}
