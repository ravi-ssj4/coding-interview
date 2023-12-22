class Solution:
    """
    method : Almost same as Subsets I(backtracking) + sorting (duplicate avoidance) + we cannot take any number unlimited number of times!
    algo:

    time: O(n.logn) + O(n.2^n) = O(n.2^n)
    space: O(n)
    """

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        cur = []
        res = []

        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            # [1, 1, 2, 2, 3]
            #  i
            # inclusion of ith element: '1'
            cur.append(candidates[i])
            dfs(
                i + 1, total + candidates[i]
            )  # this is different from Subsets I because in the problem its mentioned that each number may only be used once, but in Subsets I we were allowed to take a number unlimited number of times

            while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # exclusion of '1'
            cur.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res


"""
Basic Test Case:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Expected Output: [[1,1,6], [1,2,5], [1,7], [2,6]]

Test Case With Duplicates in Candidates:

Input: candidates = [2,5,2,1,2], target = 5
Expected Output: [[1,2,2], [5]]

Test Case With No Solution:

Input: candidates = [2,4,6], target = 5
Expected Output: []

Test Case Where Single Candidate Equals Target:

Input: candidates = [3,1,3,5,1], target = 5
Expected Output: [[5]]

Test Case With All Candidates Identical:

Input: candidates = [1,1,1,1,1], target = 3
Expected Output: [[1,1,1]]

Test Case With Target Zero:

Input: candidates = [1,2,3], target = 0
Expected Output: []

Test Case With Negative Numbers (if allowed by problem definition):

Input: candidates = [-1,1,2,5], target = 6
Expected Output: [[1,5]] or [[1,2,3]] depending on if negative numbers are considered valid candidates.

Test Case With Target Less Than Smallest Candidate:

Input: candidates = [4,3,2], target = 1
Expected Output: []

Test Case With Empty Candidates Array:

Input: candidates = [], target = 7
Expected Output: []

Test Case With Target Equal to Sum of All Candidates:

Input: candidates = [2,3,6,7], target = 18
Expected Output: [[2,2,2,2,2,2,3,3], [2,2,2,2,3,7], [2,2,2,3,3,6], [2,3,6,7]] assuming all candidates can be used as many times but only once per combination and the problem allows for all to be summed up to the target.
"""
