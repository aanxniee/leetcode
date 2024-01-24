class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        def find(board, i, j, word):

            if not len(word):
                return True

            if i >= m or i < 0 or j >= n or j < 0 or board[i][j] != word[0]:
                return False

            ret = False
            board[i][j] = "."

            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ret = find(board, i+dx, j+dy, word[1:])
                
                if ret:
                    break

            board[i][j] = word[0]
            return ret


        if not board:
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if find(board, i, j, word):
                        return True
        return False
        