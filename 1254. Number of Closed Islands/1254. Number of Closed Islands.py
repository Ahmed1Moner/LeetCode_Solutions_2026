#
# Problem: 1254. Number of Closed Islands
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-closed-islands/description/
# Language: python3
# Date: 2026-02-26


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return False

            if grid[r][c]==1:
                return True
            grid[r][c]=1

            dr=[0,1,-1,0]
            dc=[1,0,0,-1]
            closedIsland=True

            for d in range(4):
                if not dfs(r+dr[d],c+dc[d]):
                    closedIsland=False
            
            return closedIsland


        rows,cols=len(grid),len(grid[0])
        ctr=0

        for i in range(1,rows-1):
            for j in range(1,cols-1):
                if grid[i][j]==0 and dfs(i,j):
                    ctr+=1

        return ctr
