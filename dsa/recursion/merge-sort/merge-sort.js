#!/usr/bin/env node
/* Algorithm
 * If only 1 element remaining, return (its already sorted)
 * else
 *   Sort the left half
 *   Sort the right half
 *   Merge them together
 */

// returns 1 merged array
function merge(array1, array2) {
    let mergedArray = [];

    // run till one of the arrays has length 0
    while (array1.length !== 0 && array2.length !== 0) {
        if (array1[0] <= array2[0]) {
            mergedArray.push(array1.shift());
        } else {
            mergedArray.push(array2.shift());
        }
    }

    if (array1.length === 0) {
        mergedArray = mergedArray.concat(array2);
    }

    if (array2.length === 0) {
        mergedArray = mergedArray.concat(array1);
    }

    return mergedArray;
}

// returns a merged array
function mergeSort(array) {
    if (array.length === 1) return array;

    const midPoint = Math.ceil(array.length / 2);
    // slice is exclusive of the latter value
    const sortedLeft = mergeSort(array.slice(0, midPoint));
    const sortedRight = mergeSort(array.slice(midPoint, array.length));

    return merge(sortedLeft, sortedRight);
}

//console.log("");
//console.log("       Test:");
//console.log("--------------------");
//console.log(mergeSort([3, 2, 1, 13, 8, 5, 0, 1]));
//console.log(mergeSort([105, 79, 100, 110]));
//console.log(mergeSort([8, 5, 6, 3, 9]));

export default mergeSort;
