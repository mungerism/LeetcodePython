"""
17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class Solution:

    def combine(self, letters_1, letters_2):
        result = []
        if len(letters_1) == 0 | len(letters_2) == 0:
            return result

        for letter_1 in letters_1:
            for letter_2 in letters_2:
                letter = letter_1 + letter_2
                result.append(letter)

        return result


    def letterCombinations(self, digits: 'str') -> 'List[str]':
        digits_len = len(digits)

        if digits_len == 0:
            return []

        dictionary = {
            '0': [],
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        combine_result = dictionary[digits[0]]

        for i in range(1, digits_len):
            combine_result = self.combine(combine_result, dictionary[digits[i]])

        return combine_result


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('2'))
