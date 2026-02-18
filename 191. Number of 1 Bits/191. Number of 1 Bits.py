#
# Problem: 191. Number of 1 Bits
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-1-bits/
# Language: python3
# Date: 2026-02-18


#try divide and conquer and xor

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        #sol 1: O(k) time & O(k) space -> k=logn & k:num of bits

        return bin(n)[2:].count('1')
