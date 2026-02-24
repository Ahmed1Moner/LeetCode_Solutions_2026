#
# Problem: 1034. Coloring A Border
# Difficulty: Medium
# Link: https://leetcode.com/problems/coloring-a-border/description/
# Language: python3
# Date: 2026-02-24


#try bfs

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:

        #sol 1: 
        
        def dfs(r,c):
            
            visited[r][c]=True
            isBorder=False

            dr=[0,1,0,-1]
            dc=[1,0,-1,0]

            for d in range(4):
                nr,nc = r+dr[d],c+dc[d]

                if nr<0 or nr>=rows or nc<0 or nc>=cols:
                    isBorder=True
                elif grid[nr][nc]!=oldColor:
                    isBorder=True
                elif not visited[nr][nc]:
                    dfs(nr,nc)
                
            if isBorder:
                borders.append((r,c))


        
        rows,cols=len(grid),len(grid[0])
        oldColor=grid[row][col]

        visited=[[False for _ in range(cols)] for _ in range(rows)]
        borders=[]

        dfs(row,col)

        for r,c in borders:
            grid[r][c]=color

        return grid
