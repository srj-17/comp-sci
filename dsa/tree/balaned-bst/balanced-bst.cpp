// algorithm to create a balanced bst from a sorted array
#include "../bst/traversal.h"
#include <stdio.h>
#include <stdlib.h>

node *newNode(int data) {
  node *temp = (node *)malloc(sizeof(node));
  temp->data = data;
  temp->left = NULL;
  temp->right = NULL;

  return temp;
}

node *createBalancedBst(int *arr, int start, int end) {
  if (start > end)
    return NULL;

  int mid = (start + end) / 2;

  node *root = newNode(arr[mid]);
  root->left = createBalancedBst(arr, start, mid - 1);
  root->right = createBalancedBst(arr, mid + 1, end);
  return root;
}

int main() {
  int arr[] = {1, 2, 3, 4, 5, 6, 7};
  int n = sizeof(arr) / sizeof(arr[0]);

  node *root = createBalancedBst(arr, 0, n - 1);
  inOrderTraversal(root);
  printf("\n");
  return 0;
}
