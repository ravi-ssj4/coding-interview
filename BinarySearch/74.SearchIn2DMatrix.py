class Solution:
    '''
    method 1: brute force -> O(m.n)

    method 2: search top right and converge inside matrix
    idea:
        1. compare target with top right element
            if target < topRight element, then eliminate that column and continue search
            if target > topRight element, then eliminate that row and continue search
    algo:
        1. i, j = 0, len(nums[0]) - 1 (top right index)
        2. while i < len(nums) and j >= 0:
            2.1. if target < nums[i][j]:
                    j -= 1
                elif target > nums[i][j]:
                    i += 1
                else:
                    return true
        3. return false
                
    time: O(m + n) worst case: either target is found before we reach bottom left or target not present
    space: O(1)



    method 3: double binary search (BEST METHOD ALERT)
                first, vertically to get the correct row
                then, horizontally within that row to get the correct cell
    algo:
        1. initialize top, bottom = 0, len(matrix) - 1
        2. while top <= bottom:
            2.1. get middle row = (top + bottom) // 2 or top + ((bottom - top) // 2) 
            2.2. if target > last element in this row, (means the element must be in the rows below)
                    top = row + 1
                 elif target < first element in this row, (means the target must be in the rows above)
                    bottom = row - 1
                 else: break (means we have landed on the correct row)
        3. we are out of the loop means either we landed on the correct row or we didn't find any row where
           target could be present
           ie. if top > bottom: return False
        4. now initialize left = 0 and right = len(matrix[0]) - 1
        5. row = top + bottom // 2 (as we had lost reference to this as row was a local var to the first loop)
        5. while left <= right:
            5.1. middle = left + ((right - left) // 2)
            5.2. if target > matrix[row][middle]:
                    left = middle + 1
                elif target < matrix[row][middle]:
                    right = middle - 1
                else:
                    return True
        6. return False

    time: O(logn + logm)
    space: O(1)
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        # need to make sure we actually got a legitimate row
        # can do so by checking if loop terminated because 
        # top and bottom crossed each other
        if top > bottom:
            return False
        
        row = (top + bottom) // 2

        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            middle = (left + right) // 2
            if target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True
        return False