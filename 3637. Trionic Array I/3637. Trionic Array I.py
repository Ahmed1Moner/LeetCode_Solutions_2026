#
# Problem: 3637. Trionic Array I
# Difficulty: Easy
# Link: https://leetcode.com/problems/trionic-array-i/?envType=daily-question&envId=2026-02-03
# Language: python3
# Date: 2026-02-03


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:

        #sol 1: O(n) time & O(1) space
        
        i,size=0,len(nums)
        
        while i<size-1 and nums[i]<nums[i+1]:
            i+=1
        if i==0 or i==size-1: return False

        j=i
        while i<size-1 and nums[i]>nums[i+1]:
            i+=1
        if i==j or i==size-1: return False

        while i<size-1 and nums[i]<nums[i+1]:
            i+=1
        
        return i==size-1
