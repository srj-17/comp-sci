#include "traversal.h"
#include <queue>
#include <stdio.h>

void inOrderTraversal(node *root) {
  if (root == NULL) {
    return;
  }
  inOrderTraversal(root->left);
  printf("%d\t", root->data);
  inOrderTraversal(root->right);
}

void preOrderTraversal(node *root) {
  if (root == NULL) {
    return;
  }

  printf("%d\t", root->data);
  preOrderTraversal(root->left);
  preOrderTraversal(root->right);
}

void postOrderTraversal(node *root) {
  if (root == NULL) {
    return;
  }

  postOrderTraversal(root->left);
  postOrderTraversal(root->right);
  printf("%d\t", root->data);
}

void BFSTraversal(node *root) {
  if (root == NULL)
    return;

  std::queue<node *> Q;
  Q.push(root);

  while (!Q.empty()) {
    node *current = Q.front();
    printf("%d\t", current->data);

    if (current->left != NULL)
      Q.push(current->left);
    if (current->right != NULL)
      Q.push(current->right);

    // Q.front() doesn't remove element from the front
    Q.pop();
  }
}
