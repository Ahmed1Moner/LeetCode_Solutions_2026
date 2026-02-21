#
# Problem: 733. Flood Fill
# Difficulty: Easy
# Link: https://leetcode.com/problems/flood-fill/description/
# Language: python3
# Date: 2026-02-21


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        #sol 1: O(n*m) time and O(n*m) space

        def isValid(image,r,c):
            if r<0 or r>=len(image) or c<0 or c>=len(image[0]):
                return False
            return True

        def dfs(image,r,c,oldColor,newColor):
            if not isValid(image,r,c) or image[r][c]!=oldColor or visited[r][c]:
                return

            visited[r][c]=True
            image[r][c]=newColor

            dfs(image,r-1,c,oldColor,newColor)
            dfs(image,r+1,c,oldColor,newColor)
            dfs(image,r,c-1,oldColor,newColor)
            dfs(image,r,c+1,oldColor,newColor)

        
        visited=[[False for _ in range(len(image[0]))] for _ in range(len(image))]
        oldColor=image[sr][sc]


        dfs(image,sr,sc,oldColor,color)
        return image

