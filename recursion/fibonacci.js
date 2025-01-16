#!/usr/bin/env node

// param = number
// return value = array with that many numbers from fibonacci sequence
function fibs(n) {
    let array = [];
    for (let i = 0; i < n; i++) {
        if (i === 0) array = array.concat(0);
        else if (i == 1) array = array.concat(1);
        else array = array.concat(array[i - 1] + array[i - 2]);
    }
    return array;
}

// same as above, but recursive
function fibsRec(n) {
    if (n === 1) return [0];
    if (n === 2) return [0, 1];

    // just doing this so that the fibsRec(n-1) doesn't need to run twice
    const lastFibsArr = fibsRec(n - 1);
    const fibsArrayBeforeLast = fibsRec(n - 2);
    return lastFibsArr.concat(lastFibsArr.at(-1) + fibsArrayBeforeLast.at(-1));
}

const INPUT = 8;
console.log(fibs(INPUT));
console.log(fibsRec(INPUT));
