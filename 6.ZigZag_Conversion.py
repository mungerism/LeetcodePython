"""
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        matrix = [[x for x in range(numRows)] for x in range(numRows)]

        i = 0
        while i < len(s):
            for row in range(numRows):
                for column in range(numRows):
                    matrix[row][column] = s[i]
                    i += 1


if __name__ == '__main__':
    solution = Solution()
    solution.convert('abcdefghijklmn', 3)


