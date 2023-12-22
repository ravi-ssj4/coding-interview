class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set()
        posDiag = set()
        negDiag = set()
        board = [n * ["."] for _ in range(n)]

        def backtrack(r):
            if (
                r == n
            ):  # we know that we have placed all the queens at correct positions
                boardcopy = ["".join(board[row]) for row in range(n)]
                res.append(boardcopy)
                return

            for c in range(n):
                if c in cols or (r + c) in negDiag or (r - c) in posDiag:
                    continue

                # place the queen and update all 4 data structures
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r - c)
                negDiag.add(r + c)

                # call the recursive function on the next row
                backtrack(r + 1)

                # backtrack: bring back all 4 data structures back to previous state or values
                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r - c)
                negDiag.remove(r + c)

        backtrack(0)
        return res


"""
The time complexity of the N-Queens problem is a bit complex to analyze because it depends on the size of the
board (N) and the number of valid arrangements possible, which is not a straightforward calculation. 

The problem is solved using backtracking, and here's how you would generally analyze the time complexity for such an algorithm:

1. Number of Possibilities: In the worst case, you would try to place queens in all 2N2cells of the board (N rows × N columns).

2. Backtracking Pruning: However, due to backtracking, you don't explore every possibility. Once you place a queen, you only attempt
 to place another queen in valid positions. For the first queen, you have N possibilities (since you're placing one queen per row, 
 and there are N rows). 
 For the second queen, you have at most  −1N−1possibilities, and so on. 
 But due to the constraints (no two queens can be in the same row, column, or diagonal), many of these possibilities are pruned, and you never explore them.

3. Recursion: The algorithm goes as deep as N levels since there are N rows in which to place queens.
So the crude upper bound on the time complexity is  ( !)O(N!), because for each row you're placing a queen, you have N choices for the first queen,  −1N−1for the second,  −2N−2for the third, and so on, down to 1 for the last queen. 
This gives us  ×( −1)×( −2)×…×2×1= !N×(N−1)×(N−2)×…×2×1=N!arrangements to check in the worst case.

However, this upper bound is very loose because the backtracking algorithm prunes many branches of the search space. 
In practice, the algorithm is faster than  ( !)O(N!), but we still consider  ( !)O(N!)as the worst-case time complexity
because it reflects the number of possible placements of N queens on an N×N board without considering the pruning.
The exact number of valid solutions for N-Queens grows with N and does not have a simple closed-form formula, 
but it's much less than  !N!. The actual time complexity is determined by the number of these valid solutions 
and the efficiency of the pruning steps in the backtracking algorithm
"""


"""
Minimum Input:

Input: 1
Expected Output: [["Q"]]
Explanation: There is only one queen and one cell on the board, so the queen is placed there.

Impossible Scenario:

Input: 2
Expected Output: []
Explanation: It's not possible to place two queens on a 2x2 board without them threatening each other.

Another Impossible Scenario:

Input: 3
Expected Output: []
Explanation: It's also not possible to place three queens on a 3x3 board without them threatening each other.

First Non-trivial Case:

Input: 4
Expected Output: [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
Explanation: There are two distinct solutions to the 4-queens problem.

General Case:

Input: 8
Expected Output: A list of all solutions to the 8-queens problem.
Explanation: This is the classic N-Queens problem, and there are 92 solutions.

Larger Board:

Input: 10
Expected Output: A list of all solutions to the 10-queens problem.
Explanation: The number of solutions increases significantly as N grows.

Edge Case with No Input:

Input: 0
Expected Output: []
Explanation: If no queens are to be placed, the output should reflect that no solutions are needed.
Invalid Input:

Input: -1 (or any negative number)
Expected Output: This depends on the error handling in the function. It could be an empty list, or the function could raise an error.

Testing Efficiency:

Input: 12 or larger
Expected Output: A list of all solutions to the 12-queens problem.
Explanation: Inputs like this are used to test the efficiency of the algorithm as the complexity increases exponentially with larger N.
"""
