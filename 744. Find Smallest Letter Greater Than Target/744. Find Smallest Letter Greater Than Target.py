#
# Problem: 744. Find Smallest Letter Greater Than Target
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/?envType=daily-question&envId=2026-01-31
# Language: python3
# Date: 2026-01-31


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        #sol 1: O(n) time & O(1) space

        return next((ch for ch in letters if ord(ch)-ord(target)>=1), letters[0])
