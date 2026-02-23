#
# Problem: 28. Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/1929016638/
# Language: python3
# Date: 2026-02-23


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        #sol 3: O(n*m) time & O(1) space

        i=0
        n,m=len(haystack),len(needle)

        while i<n-m+1:
            j=0
            while j<m and needle[j]==haystack[j+i]:
                j+=1

            if j==m:
                return i
            i+=1

        return -1


        #sol 2: O(n) time & O(1) space

        return haystack.find(needle)


        #sol 1: O(n*m) time & O(1) space

        for i in range(len(haystack)-len(needle)+1):
            if needle==haystack[i:i+len(needle)]:
                return i
        return -1
