#
# Problem: 1905. Count Sub Islands
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-sub-islands/description/
# Language: python3
# Date: 2026-02-22


#try bfs, union find, dp solutions

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        rows,cols = len(grid2),len(grid2[0])
        dr=[-1,0,1,0]
        dc=[0,-1,0,1]

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid2[r][c]==0:
                return True

            grid2[r][c]=0
            validSubIsland=True

            #base case
            if grid1[r][c]==0:
                validSubIsland=False

            for d in range(4):
                if not dfs(r+dr[d], c+dc[d]):
                    validSubIsland=False

            return validSubIsland


        ctr=0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c]==1:
                    if dfs(r,c)==1:
                        ctr+=1

        return ctr
