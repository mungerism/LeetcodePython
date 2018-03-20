'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        dic = {}
        for i in range(numRows):
            dic[i] = []

        j = 0
        a = 1
        for c in s:
            list = dic[j]
            list.append(c)
            j += a
            if j >= numRows:
                j -= 2
                a *= -1
            if j < 0:
                j += 2
                a *= -1

        result = ''
        for i in range(numRows):
            result = result + ''.join(dic[i])

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 3))

