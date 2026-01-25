#
# Problem: 2733. Neither Minimum nor Maximum
# Difficulty: Easy
# Link: https://leetcode.com/problems/neither-minimum-nor-maximum/
# Language: python3
# Date: 2026-01-25


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:

        #Sol 2: O(n) time & O(1) space
        
        #quick skip
        if len(nums)<=2:
            return -1
        
        minVal,maxVal=min(nums),max(nums)
        return next((num for num in nums if num!=minVal and num!=maxVal),-1)



        #Sol 1: O(nlogn) time & O(1) space

        #quick skip
        if len(nums)<=2:
            return -1
        
        else:
            nums.sort()
            return nums[1]
