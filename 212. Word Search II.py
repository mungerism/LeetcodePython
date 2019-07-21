class Solution:
    def findWords(self, board, words):

        root = {}
        current_node = root

        end_of_word = '#'

        for word in words:
            current_node = root
            for char in word:
                char_node = current_node.get(char)
                if not char_node:
                    char_node = {}
                    current_node[char] = char_node
                current_node = char_node
            current_node[end_of_word] = end_of_word

        return root


if __name__ == '__main__':
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]

    solution = Solution()
    solution.findWords(board, words)
