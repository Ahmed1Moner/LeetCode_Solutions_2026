#
# Problem: 1758. Minimum Changes To Make Alternating Binary String
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2026-03-05
# Language: python3
# Date: 2026-03-05


class Solution:
    def minOperations(self, s: str) -> int:
        
        #sol 1: O(n) time & O(1) space

        ctr1=ctr2=0
        for i,num in enumerate(s):
            #0101 pattern
            if num!=str(i%2):
                ctr1+=1
        
            #1010 pattern
            if num!=str((i+1)%2):
                ctr2+=1

        return min(ctr1,ctr2)
