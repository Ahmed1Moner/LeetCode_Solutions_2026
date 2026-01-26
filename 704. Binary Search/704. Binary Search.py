#
# Problem: 704. Binary Search
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-search/submissions/1897246608/
# Language: python3
# Date: 2026-01-26


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Sol 1: O(logn) time & O(1) space

        #quick skip
        if target<nums[0] or target>nums[-1]:
            return -1

        left,right=0,len(nums)-1

        while left<=right:
            mid=(left+right)//2

            #base case
            if nums[mid]==target:
                return mid
            
            elif nums[mid]<target:
                left=mid+1
            
            elif nums[mid]>target:
                right=mid-1


        return -1
