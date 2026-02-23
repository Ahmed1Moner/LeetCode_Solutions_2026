#
# Problem: 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/
# Language: python3
# Date: 2026-02-23


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        


        #sol 1: O(n^2) time & O(1) space

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

        return -1
