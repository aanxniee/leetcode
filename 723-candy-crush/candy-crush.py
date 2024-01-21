class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """

        rows = len(board)
        cols = len(board[0])

        # finds the cells we need to crush
        def find():
            to_crush = set()

            # finds horizontal trios
            for r in range(1, rows-1):
                for c in range(cols):

                    if board[r][c] == 0:
                        continue

                    if (board[r][c] == board[r-1][c] and board[r][c] == board[r+1][c]):
                        to_crush.add((r, c))
                        to_crush.add((r-1, c))
                        to_crush.add((r+1, c))

            # finds vertical trios
            for r in range(rows):
                for c in range(1, cols-1):

                    if board[r][c] == 0:
                        continue

                    if (board[r][c] == board[r][c-1] and board[r][c] == board[r][c+1]):
                        to_crush.add((r, c))
                        to_crush.add((r, c-1))
                        to_crush.add((r, c+1))

            return to_crush

        # crushes the cells found by setting it to 0
        def crush(to_crush):

            for (r,c) in to_crush:
                board[r][c] = 0

        # bubble 0s to the top to "drop" non 0 cells
        def drop():

            # column dependent
            for c in range(cols):
                zero = -1

                # iterate through the column bottom up
                for r in range(rows-1, -1, -1):

                    # find the lowest zero and swap that 0 with other cells until it is at the top
                    if board[r][c] == 0:
                        zero = max(zero, r)

                    elif zero >= 0:
                        board[r][c], board[zero][c] = board[zero][c], board[r][c]
                        zero -= 1

        # find cells to crush, crush them, drop them and continue until the board is stable
        to_crush = find()
        while to_crush:
            crush(to_crush)
            drop()
            to_crush = find()

        return board


        

        


        
        