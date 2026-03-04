#
# Problem: 1582. Special Positions in a Binary Matrix
# Difficulty: Easy
# Link: https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/?envType=daily-question&envId=2026-03-04
# Language: python3
# Date: 2026-03-04


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        #sol 3: O(n*(n+m)) time & O(1) space
        
        def validCol(j): #O(n) time & O(1) space
            return sum(row[j] for row in mat)==1

        special=0
        for row in mat:
            if sum(row)==1: #O(m) time & O(1) space
                idx=row.index(1) #O(m) time & O(1) space
                special+=validCol(idx) #O(n) time & O(1) space

        return special


        #sol 2: O(n*m) time & O(n+m) space

        special,rows,cols=0,len(mat),len(mat[0])
        rowSum,colSum=[0]*rows,[0]*cols

        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==1:
                    rowSum[i]+=1
                    colSum[j]+=1

        
        for i in range(rows):
            for j in range(cols):
                special+=(mat[i][j]==1 and rowSum[i]==1 and colSum[j]==1)

        return special




        #sol 1: O(n*m * (n+m)) time & O(1) space

        def validRow(row): #O(m) time & O(1) space
            return row.count(1)==1

        def validCol(j): #O(m) time & O(1) space
            return sum(mat[row][j] for row in range(rows))==1


        special,rows,cols=0,len(mat),len(mat[0])
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==1:
                    if validRow(mat[i]) and validCol(j):
                        special+=1

        return special
