// implementation of rail fence cipher
#include <bits/stdc++.h>
#include <cstdio>
#include <string>

using namespace std;

string encrypt(string text, int key) {
  // first build a fence with depth = key
  // length = text length
  const int fence_width = text.length();
  const int fence_height = key;
  char fence[fence_height][fence_width];

  for (int i = 0; i < fence_height; i++)
    for (int j = 0; j < fence_width; j++)
      fence[i][j] = '\n';

  bool directionDown = false;
  int row = 0, col = 0;
  const int textLength = text.length();

  for (int i = 0; i < textLength; i++) {
    // change the direction at the top and bottom of fence (like ping pong)
    if (row == 0 || row == key - 1)
      directionDown = !directionDown;

    // col++ first completes the assignment and assigns the incremented value to
    // col
    fence[row][col++] = text[i];

    directionDown ? row++ : row--;
  }

  string result;
  for (int i = 0; i < fence_height; i++)
    for (int j = 0; j < fence_width; j++)
      if (fence[i][j] != '\n')
        result.push_back(fence[i][j]);

  return result;
}

string decrypt(string text, int key) {
  // first build a fence with depth = key
  // length = text length
  const int fence_width = text.length();
  const int fence_height = key;
  char fence[fence_height][fence_width];
  const int textLength = text.length();

  // build the fence
  for (int i = 0; i < fence_height; i++)
    for (int j = 0; j < fence_width; j++)
      fence[i][j] = '\n';

  bool directionDown = false;
  int row = 0, col = 0;
  // place * in the positions where ciphertext will go
  for (int i = 0; i < fence_width; i++) {
    if (row == 0 || row == key - 1)
      directionDown = !directionDown;

    fence[row][col++] = '*';

    directionDown ? row++ : row--;
  }

  // put ciphertext in those positions
  int index = 0;
  for (int i = 0; i < fence_height; i++)
    for (int j = 0; j < fence_width; j++)
      if (fence[i][j] == '*' && index < textLength)
        fence[i][j] = text[index++];

  // find plainText
  string result;
  directionDown = false, row = 0, col = 0;
  for (int i = 0; i < textLength; i++) {
    if (row == 0 || row == fence_height - 1)
      directionDown = !directionDown;

    if (fence[row][col] != '*')
      result.push_back(fence[row][col++]);

    directionDown ? row++ : row--;
  }

  return result;
}

int main() {
  string plainText, cipherText;
  int key;
  cout << "Enter text: ";
  getline(cin, plainText);
  cout << "Enter key: ";
  cin >> key;
  cipherText = encrypt(plainText, key);
  cout << "The cipher text is: " << cipherText << endl;
  cout << "Back to plainText: " << decrypt(cipherText, key) << endl;

  return 0;
}
