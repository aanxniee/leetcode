class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """

        rows = len(board)
        cols = len(board[0])

        # finds the cells we need to crush and crushes them
        def find_and_crush():
            
            done = True

            # finds horizontal trios
            for r in range(1, rows-1):
                for c in range(cols):

                    if board[r][c] == 0:
                        continue
                    
                    # set trios to their negative value to look for combos with > 3 (we just look for 3 at once)
                    # ie. 1 1 1 1 1 --> -1 -1 -1 1 1 (5 will still get crushed)
                    if (abs(board[r][c]) == abs(board[r-1][c]) and abs(board[r][c]) == abs(board[r+1][c])):
                        board[r][c] = -abs(board[r][c])
                        board[r+1][c] = -abs(board[r+1][c])
                        board[r-1][c] = -abs(board[r-1][c])

                        done = False

            # finds vertical trios
            for r in range(rows):
                for c in range(1, cols-1):

                    if board[r][c] == 0:
                        continue

                    if (abs(board[r][c]) == abs(board[r][c-1]) and abs(board[r][c]) == abs(board[r][c+1])):
                        board[r][c] = -abs(board[r][c])
                        board[r][c-1] = -abs(board[r][c-1])
                        board[r][c+1] = -abs(board[r][c+1])

                        done = False

            # crush them
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] < 0:
                        board[r][c] = 0

            return done

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
        while not find_and_crush():
            drop()

        return board


        

        


        
        