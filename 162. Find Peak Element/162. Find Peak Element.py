#
# Problem: 162. Find Peak Element
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-peak-element/
# Language: python3
# Date: 2026-02-01


#solv 941 &e 852 first


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        #sol 2: O(logn) time & O(1) space (edges included)

        left,right=0,len(nums)-1
        while left<right:

            mid=left+(right-left)//2

            if nums[mid]<nums[mid+1]:
                left=mid+1
            
            elif nums[mid]>nums[mid+1]:
                right=mid

        return left



        #sol 1: O(n) time & O(1) space

        return nums.index(max(nums))
