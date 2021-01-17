// 628. Maximum Product of Three Numbers
// Easy
//
// 1416
//
// 417
//
// Add to List
//
// Share
// Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
//
//
//
// Example 1:
//
// Input: nums = [1,2,3]
// Output: 6
// Example 2:
//
// Input: nums = [1,2,3,4]
// Output: 24
// Example 3:
//
// Input: nums = [-1,-2,-3]
// Output: -6

const maximumProduct = (nums) => {
  nums = nums.sort((a, b) => a - b)
  let len = nums.length - 1
  let product1 = nums[0] * nums[1] * nums[2]
  let product2 = nums[0] * nums[1] * nums[len]
  let product3 = nums[len] * nums[len - 1] * nums[len - 2]

  return Math.max(product1, product2, product3)
}


let nums = [-100, -98, -1, 2, 3, 4]
// nums = [1, 2, 3, 4]
console.log(`maximumProduct: ${maximumProduct(nums)}`)



