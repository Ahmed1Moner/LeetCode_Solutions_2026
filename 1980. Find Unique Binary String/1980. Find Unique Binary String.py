#
# Problem: 1980. Find Unique Binary String
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-unique-binary-string/?envType=daily-question&envId=2026-03-08
# Language: python3
# Date: 2026-03-08


#try backtracking & recursion

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        #sol 3: O(n) time & O(n) space

        return ''.join('1' if nums[i][i]=='0' else '0' for i in range(len(nums))) #Cantor's diagonal argument


        #sol 2: O(n*(2**n)) time & O(n*(2**n)) space

        return next((''.join(bit) for bit in product('01',repeat=len(nums)) if ''.join(bit) not in nums), None)

        #sol 1: O(n*(2**n)) time & O(n*(2**n)) space

        codes=[format(i,f"0{len(nums)}b") for i in range(2**len(nums))]
        return next((c for c in codes if c not in nums),None)

