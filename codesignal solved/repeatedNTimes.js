// 961. N-Repeated Element in Size 2N Array
// Easy
//
// 577
//
// 254
//
// Add to List
//
// Share
// In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
//
// Return the element repeated N times.
//
//
//
// Example 1:
//
// Input: [1,2,3,3]
// Output: 3
// Example 2:
//
// Input: [2,1,2,5,3,2]
// Output: 2
// Example 3:
//
// Input: [5,1,5,2,5,3,5,4]
// Output: 5

const repeatedNTimes = (arr) => {
//  find n by getting length of array / 2
  let n = arr.length / 2
//  find the number in the array repeated n times
  let numCount = {}
  for (let i = 0; i < n * 2; i ++) {
    if (!(arr[i] in numCount)) {
      numCount[arr[i]] = 0
    }
    numCount[arr[i]] += 1
  }
  console.log({numCount})
  for (const key in numCount) {
    console.log({key})
    console.log(numCount[key])
    if (numCount[key] === n ) {
      return key
    }
  }
}

const arr = [1,2,3,3]
console.log(repeatedNTimes(arr))
