#
# Problem: 693. Binary Number with Alternating Bits
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-number-with-alternating-bits/description/?envType=daily-question&envId=2026-02-18
# Language: python3
# Date: 2026-02-18


#try xor

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        #sol 5: O(n) time & O(1) space
        
        num=bin(n)[2:]
        return all(a!=b for a,b in pairwise(num))


        #sol 4: O(n) time & O(n) space

        num=bin(n)[2:]
        return all(a!=b for a,b in zip(num,num[1:]))


        #sol 3: O(n) time & O(1) space

        num=bin(n)[2:]
        return next((False for i in range(len(num)-1) if num[i]==num[i+1]), True)


        #sol 2: O(n) time & O(1) space

        num=bin(n)[2:]
        return all(num[i]!=num[i+1] for i in range(len(num)-1))


        #sol 1: O(n) time & O(1) space

        num=bin(n)[2:]

        for i in range(len(num)-1):
            if num[i]==num[i+1]:
                return False

        return True
