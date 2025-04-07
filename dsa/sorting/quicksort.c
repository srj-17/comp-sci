#include <stdio.h>

void swap(int *x, int *y) {
  int temp = *x;
  *x = *y;
  *y = temp;
}

void printArray(int arr[], int n) {
  for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }
}

int partition(int A[], int l, int r) {
  int x = l;
  int y = r;
  int p = A[l];
  while (x < y) {
    // find out of place elements (elements that are not in the
    // sub-array they're supposed to be in)
    // i.e. smaller elements in sub-array composed of greater elements
    // right of the pivot
    // and vice versa
    while (A[x] <= p && x < r)
      x++;
    while (A[y] >= p && y > l)
      y--;
    if (x < y)
      swap(&A[x], &A[y]);
  }
  // swap the partition with the current element in the current
  // position of y
  swap(&A[y], &A[l]);

  // return position of partition
  return y;
}

void quickSort(int A[], int l, int r) {
  if (l < r) {
    int p = partition(A, l, r);
    quickSort(A, l, p - 1);
    quickSort(A, p + 1, r);
  }
}

int main() {
  int arr[] = {5, 3, 8, 1, 4};
  int n = sizeof(arr) / sizeof(arr[0]);
  printf("Unsorted array: \n");
  printArray(arr, n);

  quickSort(arr, 0, n - 1);

  printf("\nSorted array: \n");
  printArray(arr, n);

  return 0;
}
