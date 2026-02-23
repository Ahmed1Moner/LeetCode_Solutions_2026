#
# Problem: 66. Plus One
# Difficulty: Easy
# Link: https://leetcode.com/problems/plus-one/description/
# Language: python3
# Date: 2026-02-23


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        #sol 1: O(n) time & O(1) space

        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits

            digits[i]=0

        digits.insert(0,1)
        return digits
