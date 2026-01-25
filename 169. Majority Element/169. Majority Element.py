#
# Problem: 169. Majority Element
# Difficulty: Easy
# Link: https://leetcode.com/problems/majority-element/?envType=problem-list-v2&envId=w95808hv
# Language: python3
# Date: 2026-01-25


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #if appears more than half the time, it must occupy the middle position after sorting.
        nums.sort()
        return nums[len(nums)//2]


        # freq,size=Counter(nums),len(nums)

        # for k,v in freq.items():
        #     if v>(size//2):
        #         return k

        # # #TLE
        # # return next((num for num in nums if nums.count(num)>(len(nums)//2)),None)
