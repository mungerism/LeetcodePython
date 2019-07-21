class Solution:

    def __init__(self):
        self.result = []
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.length = 0
        self.width = 0

    def findWords(self, board, words):
        root_trie_node = self.generate_trie(words)

        length = len(board)
        width = len(board[0])

        for l in range(length):
            for w in range(width):
                if board[l][w] in root_trie_node:
                    self.dfs(board, l, w, "", root_trie_node)

        return self.result

    def generate_trie(self, words):
        root = {}
        for word in words:
            current_node = root
            for char in word:
                char_node = current_node.get(char)
                if not char_node:
                    char_node = {}
                    current_node[char] = char_node
                current_node = char_node
        return root

    def dfs(self, board, l, w, current_word, current_dict):
        current_word += board[l][w]
        current_dict = current_dict.get(board[l][w])

        if current_dict is None:
            return

        if not current_dict:
            self.result.append(current_word)

        tmp, board[l][w] = board[l][w], '@'
        for k in range(4):
            x, y = l + self.dx[k], w + self.dy[k]
            if 0 <= x < self.length and 0 <= y < self.width and board[x][y] != '@' and board[x][y] in current_dict:
                self.dfs(board, x, y, current_word, current_dict)
        board[l][w] = tmp

if __name__ == '__main__':
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]

    solution = Solution()
    print(solution.findWords(board, words))
