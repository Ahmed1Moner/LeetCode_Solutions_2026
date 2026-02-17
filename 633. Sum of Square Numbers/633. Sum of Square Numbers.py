#
# Problem: 633. Sum of Square Numbers
# Difficulty: Medium
# Link: https://leetcode.com/problems/sum-of-square-numbers/
# Language: python3
# Date: 2026-02-17


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        #sol 2: O(logn) time & O(1) spapce
        
        left,right=0,int(c**0.5)
        while left<=right:
            summ=left*left+right*right
            
            if summ==c:
                return True
            
            elif summ<c:
                left+=1

            else:
                right-=1

        return False


        #sol 1: brute force TLE: O(n^2) time & O(1) space

        for i in range(c+1):
            for j in range(i,c+1):
                if i*i+j*j==c:
                    return True

        return False
