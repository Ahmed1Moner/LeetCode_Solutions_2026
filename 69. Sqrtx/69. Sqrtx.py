#
# Problem: 69. Sqrt(x)
# Difficulty: Easy
# Link: https://leetcode.com/problems/sqrtx/
# Language: python3
# Date: 2026-02-17


class Solution:
    def mySqrt(self, x: int) -> int:

        #sol 1: O(logn) time & O(1) space

        if x<2: return x

        left,right=2,x//2
        while left<=right:
            mid=left+(right-left)//2

            if mid*mid==x:
                return mid

            elif mid*mid<x:
                left=mid+1
            else:
                right=mid-1

        return right #when loop ends: right<left & right is the last true
