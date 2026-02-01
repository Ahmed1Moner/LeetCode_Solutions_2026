#
# Problem: 744. Find Smallest Letter Greater Than Target
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/?envType=daily-question&envId=2026-01-31
# Language: python3
# Date: 2026-02-01


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        #sol 2: O(logn) time & O(1) space

        left,right=0,len(letters)-1
        while left<=right:
            mid=left+(right-left)//2

            if letters[mid]>target:
                right=mid-1

            else:
                left=mid+1

        return letters[left] if left<len(letters) else letters[0]




        #sol 1: O(n) time & O(1) space

        return next((ch for ch in letters if ord(ch)-ord(target)>=1), letters[0])
