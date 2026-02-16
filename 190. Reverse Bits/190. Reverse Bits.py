#
# Problem: 190. Reverse Bits
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-bits/?envType=daily-question&envId=2026-02-16
# Language: python3
# Date: 2026-02-16


#try divide and conquer & bit manipulation techniques

class Solution:
    def reverseBits(self, n: int) -> int:
        
        #sol 1: O(k) time & O(k) space: k~32

        return int(bin(n)[2:].zfill(32)[::-1],2)
