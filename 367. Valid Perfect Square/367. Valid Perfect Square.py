#
# Problem: 367. Valid Perfect Square
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-perfect-square/description/
# Language: python3
# Date: 2026-02-17


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        #sol 1: O(logn) time & O(1) space

        left,right=1,num
        while left<=right:
            mid=left+(right-left)//2

            if mid*mid==num:
                return True

            elif mid*mid<num:
                left=mid+1
            else:
                right=mid-1
        
        return False
