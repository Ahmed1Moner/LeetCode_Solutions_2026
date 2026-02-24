#
# Problem: 832. Flipping an Image
# Difficulty: Easy
# Link: https://leetcode.com/problems/flipping-an-image/description/
# Language: python3
# Date: 2026-02-24


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        #sol 1: O(m*n) time & O(1) space

        rows,cols=len(image),len(image[0])

        for r in range(rows):
            i,j=0,cols-1

            while i<=j:
                image[r][i],image[r][j]=int(not image[r][j]),int(not image[r][i])

                i+=1
                j-=1

        return image
