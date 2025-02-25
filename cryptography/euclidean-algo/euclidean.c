/*
 * euclidean algorithm is based on the fact that if we take the remainder
 * of the larger number and the smaller number the gcd of the numbers
 * don't change.
 * The algorithm also works if there smaller number is given as larger and
 * larger as smaller ex: 2, 8, 2 mod 8 is 2 and in the next step, 2 mod 2 = 0,
 * giving gcd 2
 */

#include <stdio.h>

// return the smaller number as gcd if there is no remainder
// between larger and smaller number
int gcd(int a, int b) {
  if (a == 0)
    return b;

  return gcd(b % a, a);
}

int main() {
  int x, y, d;
  printf("Program to find GCD using euclidean algorithm.\n");
  printf("Enter the larger number: ");
  scanf("%d", &x);
  printf("Enter the smaller number: ");
  scanf("%d", &y);
  d = gcd(x, y);
  printf("The GCD of the given numbers is %d\n", d);

  return 0;
}
