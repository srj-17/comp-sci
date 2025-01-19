#include <ctype.h>
#include <stdio.h>

// returns the position of found item if found, else -1
int binarySearch(int *array, int searchItem, int startIndex, int endIndex);

int main() {
  int arr[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21};
  int item, resultPos;

  // sizeof returns the size in bytes
  int n = sizeof(arr) / sizeof(arr[0]);

  printf("Enter a search item (integer): ");
  scanf("%d", &item);

  resultPos = binarySearch(arr, item, 0, n - 1);

  if (resultPos == -1) {
    printf("The search item wasn't found in the array. \n");
    return 1;
  }

  printf("The search item was found at array position %d \n", resultPos);

  return 0;
}

int binarySearch(int *array, int searchItem, int startIndex, int endIndex) {
  // truncates the decimal values
  int midPoint = (startIndex + endIndex) / 2;
  if (array[midPoint] == searchItem) {
    return midPoint;
  } else if (array[midPoint] > searchItem) {
    // was not found at midpoint, so we don't search midpoint
    endIndex = midPoint - 1;
    return binarySearch(array, searchItem, startIndex, endIndex);
  } else {
    startIndex = midPoint + 1;
    return binarySearch(array, searchItem, startIndex, endIndex);
  }
}
