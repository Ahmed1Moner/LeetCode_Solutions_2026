#
# Problem: 747. Largest Number At Least Twice of Others
# Difficulty: Easy
# Link: https://leetcode.com/problems/largest-number-at-least-twice-of-others/submissions/1896929441/
# Language: python3
# Date: 2026-01-25


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        #Sol 2: O(n) time & O(1) space
        maxVal=max(nums)
        idx=nums.index(maxVal)
        # nums.pop(idx)

        return idx if all(maxVal>=2*num for i,num in enumerate(nums) if i!=idx) else -1



        #Sol 1: O(n) time & O(1) space

        maxVal,idx=max(nums)
        idx=nums.index(maxVal)
        nums.pop(idx)

        for num in nums:
            if maxVal<2*num:
                return -1
        return idx
