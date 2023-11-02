class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # base case 1
            if total == target:
                res.append(cur.copy())
                return
            
            # base case 2
            if i >= len(candidates) or total > target:
                return

            # left side of decision tree -> include candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop() # bringing back to original state

            # right side of decision tree -> don't include candidates[i]
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
    
        return res