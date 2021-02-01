// 890. Find and Replace Pattern
// Medium
//
// 881
//
// 83
//
// Add to List
//
// Share
// You have a list of words and a pattern, and you want to know which words in words matches the pattern.
//
// A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
//
// (Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)
//
// Return a list of the words in words that match the given pattern.
//
// You may return the answer in any order.
//
//
//
// Example 1:
//
// Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
// Output: ["mee","aqq"]
// Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
// "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
// since a and b map to the same letter.

const findAndReplacePattern = (words, pattern) => {

    const createSequence = (sequence) => {
        let visited = {}
        let counter = 0
        let result = ''
        for (let i = 0; i < sequence.length; i++) {
            if (!(sequence[i] in visited)) {
                visited[sequence[i]] = counter
                counter++
                result += visited[sequence[i]].toString()
            } else {
                result += visited[sequence[i]].toString()
            }
        }
        return result
    }

    const patternSequence = createSequence(pattern)
    console.log({patternSequence});
    const resultWords = []
    for (let i = 0; i < words.length; i++) {
        console.log(words[i]);
        const wordSequence = createSequence(words[i])
        console.log({wordSequence});
        if (wordSequence === patternSequence) {
            resultWords.push(words[i])
        }
    }
    return resultWords
}

console.log(findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"));
