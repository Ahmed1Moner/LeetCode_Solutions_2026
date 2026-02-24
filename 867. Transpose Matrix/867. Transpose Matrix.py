#
# Problem: 867. Transpose Matrix
# Difficulty: Easy
# Link: https://leetcode.com/problems/transpose-matrix/description/
# Language: python3
# Date: 2026-02-24


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        #sol 1: O(n*m) time & O(n*m) space

        rows,cols=len(matrix),len(matrix[0])

        return [[matrix[r][c] for r in range(rows)] for c in range(cols)]
