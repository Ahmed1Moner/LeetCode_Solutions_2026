#
# Problem: 3010. Divide an Array Into Subarrays With Minimum Cost I
# Difficulty: Easy
# Link: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/submissions/1903693511/?envType=daily-question&envId=2026-02-01
# Language: python3
# Date: 2026-02-01


class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        #sol 2: O(n) time & O(1) space

        first=second=float('inf')

        for num in nums[1:]:
            if num<first:
                second=first
                first=num
            
            elif num<second:
                second=num
            
        return nums[0]+first+second





        #sol 1: O(nlogn) time & O(1) space

        lst=sorted(nums[1:])[:2]
        return nums[0]+lst[0]+lst[1]
