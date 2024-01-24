class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        # word param presents the characters we have left to search for
        def find(board, i, j, word):

            # base case, if len(word) = 0 then we are done searching
            if not len(word):
                return True

            # edge cases, ensure current cell is in board and that it matches the letter we are trying to find
            if i >= m or i < 0 or j >= n or j < 0 or board[i][j] != word[0]:
                return False

            ret = False
            board[i][j] = "." # mark cell as visited

            # search for next letter in the 4 directions
            # pass in word[1:] because word[0] was found
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ret = find(board, i+dx, j+dy, word[1:])
                
                if ret:
                    break

            board[i][j] = word[0] # backtrack
            return ret


        if not board:
            return False

        # traverse board
        for i in range(m):
            for j in range(n):
                    if find(board, i, j, word):
                        return True
        return False
        