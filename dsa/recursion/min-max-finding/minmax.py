"""To calculate floor mid value"""
from math import floor

def min_max(a:list[int]) -> tuple[int, int]:
    """
    Return a min, max of a list.

    A function to take a list and return a tuple
    containing (min, max) elements of the list recursively.

    Basis: If the list is of size 1, the minimum and maxmum values
    are the only element. 

    Recursive: calculate the min, max of sub-arrays until we reach
    to basis then combine the min-max by calculating the minimum and 
    maximum of the returned minimums and maximums from the sub-array.

    Then return the (minimum, maximum) to the function containing larger
    array. 

    Finally, we'll have the minimum and maximum of the whole array.
    """
    if len(a) == 1:
        minimum = maximum = a[0]
        return (minimum, maximum)

    mid = floor(len(a) / 2)
    (minimum, maximum) = min_max(a[0:mid])
    (minimum1, maximum1) = min_max(a[mid:len(a)])
    minimum = min(minimum, minimum1)
    maximum = max(maximum, maximum1)
    return (minimum, maximum)

arr = [10, 2, 3, 4, 5]
(mini, maxi) = min_max(arr)
print(mini, maxi)
