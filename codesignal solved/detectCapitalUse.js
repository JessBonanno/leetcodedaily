 //520. Detect Capital
 // Easy
 //
 // 750
 //
 // 287
 //
 // Add to List
 //
 // Share
 // Given a word, you need to judge whether the usage of capitals in it is right or not.
 //
 // We define the usage of capitals in a word to be right when one of the following cases holds:
 //
 // All letters in this word are capitals, like "USA".
 // All letters in this word are not capitals, like "leetcode".
 // Only the first letter in this word is capital, like "Google".
 // Otherwise, we define that this word doesn't use capitals in a right way.
 //
 //
 // Example 1:
 //
 // Input: "USA"
 // Output: True
 //
 //
 // Example 2:
 //
 // Input: "FlaG"
 // Output: False


 const detectCapitalUse = (word) => {
 // if all letters are capital return true
   if (word === word.toUpperCase() || word === word.toLowerCase()) {
    return true
   }
 //  if only first is capital return true
   const [firstChar, ...rest] = word
   console.log({firstChar})
  if (firstChar === firstChar.toUpperCase() && rest.join('') === rest.join('').toLowerCase()) {
    return true
  }
      return false
 }

 console.log(detectCapitalUse('FlaG'))
