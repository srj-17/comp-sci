#include "./traversal.h"
#include <stdio.h>
#include <stdlib.h>

node *getNode(int data) {
  // malloc returns a pointer to void, which should be casted in cpp, and not in
  // c, more specifically when compiled by a cpp compiler, casts are needed
  node *temp = (node *)malloc(sizeof(node));
  temp->data = data;
  temp->left = NULL;
  temp->right = NULL;

  return temp;
}

node *addNodeToBST(node *root, int data) {
  if (root == NULL) {
    node *root = getNode(data);
    return root;
  }

  if (data > root->data) {
    root->right = addNodeToBST(root->right, data);
  } else {
    root->left = addNodeToBST(root->left, data);
  }

  return root;
}

node *constructBST(int *arr, int n) {
  if (n == 0)
    return NULL;

  node *root = NULL;
  for (int i = 0; i < n; i++) {
    root = addNodeToBST(root, arr[i]);
    printf("Added %d\n", arr[i]);
  }

  return root;
}

int main() {
  int arr[] = {7, 4, 12, 3, 6, 8, 1, 5, 10};
  int n = sizeof(arr) / sizeof(arr[0]);
  node *root = constructBST(arr, n);

  printf("\nInorder traversal\n");
  inOrderTraversal(root);
  printf("\nPreorder traversal\n");
  preOrderTraversal(root);
  printf("\nPostorder traversal\n");
  postOrderTraversal(root);
  printf("\nBFS traversal\n");
  BFSTraversal(root);

  printf("\n");
  return 0;
}
