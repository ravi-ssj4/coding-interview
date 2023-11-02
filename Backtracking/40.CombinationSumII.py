class Solution:
    '''
    method : Almost same as Subsets I(backtracking) + sorting (duplicate avoidance) + we cannot take any number unlimited number of times!
    algo:

    time: O(n.logn) + O(n.2^n) = O(n.2^n)
    space: O(n)
    '''
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
            dfs(i + 1, total + candidates[i]) # this is different from Subsets I because in the problem its mentioned that each number may only be used once, but in Subsets I we were allowed to take a number unlimited number of times

            while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            # exclusion of '1'
            cur.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res