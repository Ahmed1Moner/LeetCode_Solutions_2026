#
# Problem: 852. Peak Index in a Mountain Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Language: python3
# Date: 2026-02-01


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        #sol 2: O(logn) time & O(1) space

        left,right=1,len(arr)-2 #take care: not first nor the last are peaks
        while left<=right:
            mid=left+(right-left)//2

            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            
            if arr[mid]>arr[mid+1]:
                right=mid-1
            
            elif arr[mid]>arr[mid-1]:
                left=mid+1
        
        return -1
        




        #sol 1: O(n) time & O(1) space

        return next((i for i in range(1,len(arr)-1) if arr[i]>arr[i-1] and arr[i]>arr[i+1]), -1)
