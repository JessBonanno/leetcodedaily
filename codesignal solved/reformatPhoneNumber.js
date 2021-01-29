/* 1694. Reformat Phone Number
Easy

69

81

Add to List

Share
You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.

You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes. Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits. The final digits are then grouped as follows:

2 digits: A single block of length 2.
3 digits: A single block of length 3.
4 digits: Two blocks of length 2 each.
The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1 and produce at most two blocks of length 2.

Return the phone number after formatting.



Example 1:

Input: number = "1-23-45 6"
Output: "123-456"
Explanation: The digits are "123456".
Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
Step 2: There are 3 digits remaining, so put them in a single block of length 3. The 2nd block is "456".
Joining the blocks gives "123-456".
Example 2:

Input: number = "123 4-567"
Output: "123-45-67"
Explanation: The digits are "1234567".
Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
Step 2: There are 4 digits left, so split them into two blocks of length 2. The blocks are "45" and "67".
Joining the blocks gives "123-45-67".
Example 3:

Input: number = "123 4-5678"
Output: "123-456-78"
Explanation: The digits are "12345678".
Step 1: The 1st block is "123".
Step 2: The 2nd block is "456".
Step 3: There are 2 digits left, so put them in a single block of length 2. The 3rd block is "78".
Joining the blocks gives "123-456-78".
Example 4:

Input: number = "12"
Output: "12"
Example 5:

Input: number = "--17-5 229 35-39475 "
Output: "175-229-353-94-75"
*/

/**
 * @param {string} number
 * @return {string}
 */
var reformatNumber = function (number) {

  //  remove the spaces and dashes from the number
  let cleanNumber = number.split(' ').join('')
  cleanNumber = cleanNumber.split('-').join('')
  let copyClean = cleanNumber.split('')


  // init a results string to hold our end result
  let results = ''
  // init a currentLength to store current length
  //  iterate over number
  for (let i = 0; i < cleanNumber.length; i++) {
    let curLength = copyClean.length
    if (curLength > 0) {
      // check if current length is 4 or less if so
      if (curLength < 5) {
        // handle if it is 4
        if (curLength === 4) {
          // add first 2 to results string then dash then last 2
          results += copyClean.splice(0, 2) + '-' + copyClean.splice(0, 2)
        } else if (curLength === 3) {
          // handle if it is 3
          // add all to results string
          results += copyClean.splice(0, 3)
          // handle if it is 2
          // add all to results string
        } else if (curLength === 2) {
          results += copyClean.splice(0, 2)
        }
      } else if (curLength > 4) {
        // if length is more than 4
        // add first 3 digits to results string
        // add a dash to the results string
        results += copyClean.splice(0, 3) + '-'

      }
    }
    }
  return results.replace(/,/g, '')
};

// console.log(reformatNumber("--17-5 229 35-39475 "))


