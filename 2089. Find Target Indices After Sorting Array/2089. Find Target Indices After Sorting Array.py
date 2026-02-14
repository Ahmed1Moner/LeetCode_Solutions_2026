#
# Problem: 2089. Find Target Indices After Sorting Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-target-indices-after-sorting-array/
# Language: python3
# Date: 2026-02-14


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        


        #sol 1: O(nlogn) time & O(n) space

        nums.sort()
        return [i for i,num in enumerate(nums) if num==target]
