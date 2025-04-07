#include <math.h>
#include <stdio.h>

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

void merge(int A[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];

    // Copy data into temporary arrays
    for (int i = 0; i < n1; i++)
        L[i] = A[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = A[m + 1 + j];

    // Merge temporary arrays back into A[l..r]
    int i = 0, j = 0, k = l;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            A[k] = L[i];
            i++;
        } else {
            A[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy remaining elements of L[], if any
    while (i < n1) {
        A[k] = L[i];
        i++;
        k++;
    }

    // Copy remaining elements of R[], if any
    while (j < n2) {
        A[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int A[], int l, int r) {
    if (l < r) {
        int m = (int)floor((l + r) / 2.0);

        // Recursively sort first and second halves
        mergeSort(A, l, m);
        mergeSort(A, m + 1, r);

        // Merge sorted halves
        merge(A, l, m, r);
    }
}

int main() {
    int arr[] = {5, 2, 3, 1, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Unsorted array:\n");
    printArray(arr, n);

    mergeSort(arr, 0, n - 1);

    printf("Sorted array:\n");
    printArray(arr, n);

    return 0;
}
