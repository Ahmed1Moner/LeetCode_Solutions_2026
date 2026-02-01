#
# Problem: 852. Peak Index in a Mountain Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/1904680978/
# Language: python3
# Date: 2026-02-01


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        


        #sol 1: O(n) time & O(1) space

        return next((i for i in range(1,len(arr)-1) if arr[i]>arr[i-1] and arr[i]>arr[i+1]), -1)
