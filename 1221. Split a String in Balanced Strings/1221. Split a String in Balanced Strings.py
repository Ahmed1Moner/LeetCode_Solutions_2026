#
# Problem: 1221. Split a String in Balanced Strings
# Difficulty: Easy
# Link: https://leetcode.com/problems/split-a-string-in-balanced-strings/description/?envType=problem-list-v2&envId=waksgnnd
# Language: python3
# Date: 2026-03-08


class Solution:
    def balancedStringSplit(self, s: str) -> int:

        #sol 1: O(n) time & O(1) space

        r,l,ctr=0,0,0

        for i in range(len(s)):
            if s[i]=='L':
                l+=1
            else:
                r+=1
            if l==r:
                ctr+=1
                l,r=0,0

        return ctr
