// header guards
// prevent us from declaring the header multiple times
// and prevents circular / recursive dependencies
//
// and this file contains the API that we want the program that includes
// this header to see
#ifndef TRAVERSAL_H
#define TRAVERSAL_H

typedef struct Node {
  int data;
  struct Node *left;
  struct Node *right;
} node;

void inOrderTraversal(node *root);
void preOrderTraversal(node *root);
void postOrderTraversal(node *root);
void BFSTraversal(node *root);

#endif // !TRAVERSAL_H
