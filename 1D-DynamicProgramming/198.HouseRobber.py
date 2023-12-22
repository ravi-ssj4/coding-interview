class Solution:
    def rob(self, nums: List[int]) -> int:
        # recurrance relation:
            # output[i] = max(output including current element, output excluding current element)
            #           = max((nums[i] + output[i - 2]), output[i - 1])
        
        # Eg: [ 1 ,  2  , 3 , 1]
        #      rob1,rob2,rob3
        # result (@idx = 2) = max((nums[2] + rob1), rob2);

        rob1, rob2 = 0, 0
        for n in nums:
            rob3 = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = rob3
        return rob2