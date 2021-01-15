"""
299. Bulls and Cows
Medium

858

997

Add to List

Share
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.



Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
Example 3:

Input: secret = "1", guess = "0"
Output: "0A0B"
Example 4:

Input: secret = "1", guess = "1"
Output: "1A0B"
"""

# bulls are digits in correct place
# cows are correct digits in wrong place

secret = "1122"
guess = "2211"
expected = "0A4B"
secret = "1123"
guess = "0111"
expected = "1A1B"
secret = "9305"
guess = "9205"
expected = "3A0B"


def getHint(secret, guess):
    def getBulls(secret, guess):
        # init new guess and secret
        new_guess = guess
        new_secret = secret
        # init found_bulls
        found_bulls = ''
        for i in range(len(guess)):
            # if guess and secret match at index
            if guess[i] == secret[i]:
                # add the guess to the found bulls
                found_bulls += guess[i]
                # remove the match from the guess and secret
                new_secret = new_secret.replace(secret[i], '', 1)
                new_guess = new_guess.replace(guess[i], '', 1)
        # return the bulls and the new secret and guess
        return found_bulls, new_secret, new_guess

    # helper to find cows
    def getCows(secret, guess):
        # init cows count
        cows = 0
        for i in range(len(guess)):
            # if the guess is in the secret
            if guess[i] in secret:
                # increment the cow count
                cows += 1
                # remove the guessed item from the secret
                secret = secret.replace(guess[i], '', 1)
        # return the found cows
        return cows

    # get the bulls, new secret and guess by calling getBulls helper
    bulls, new_secret, new_guess = getBulls(secret, guess)
    # get the cows by calling getCows with the new secret and guess obtained
    # from get cows
    cows = getCows(new_secret, new_guess)
    # return the length of bulls as bulls and the cows
    return f'{len(bulls)}A{cows}B'

# print(getHint(secret, guess))
