#
# Problem: 35. Search Insert Position
# Difficulty: Easy
# Link: https://leetcode.com/problems/search-insert-position/
# Language: python3
# Date: 2026-02-16


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        #sol 2: O(logn) time & O(1) space

        left,right=0,len(nums)
        while left<right:
            mid=left+(right-left)//2

            # if nums[mid]==target:
            #     return mid
            
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid

        return left


        #sol 1: O(n) time & O(1) space

        i=0
        while i<len(nums):
            if nums[i]>=target:
                return i

            i+=1

        return i #if i==len(nums)
        
