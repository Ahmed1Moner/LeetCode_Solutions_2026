#
# Problem: 1784. Check if Binary String Has at Most One Segment of Ones
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/?envType=daily-question&envId=2026-03-06
# Language: python3
# Date: 2026-03-06


#bad description
#AT MOST ONE SEGMENT

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        #sol 1: O(n) time & O(1) space

        return '01' not in s
