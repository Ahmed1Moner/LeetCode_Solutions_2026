#
# Problem: 547. Number of Provinces
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-provinces/
# Language: python3
# Date: 2026-03-07


class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        
        #sol 2: O(n^2) time & O(n) space

        def dfs(node):
            seen.add(node)
            for neighbor in range(cols):
                if neighbor not in seen and mat[node][neighbor]==1:
                    dfs(neighbor)

        
        rows,cols,ctr=len(mat),len(mat[0]),0
        seen=set()

        for city in range(rows):
            if city not in seen:
                ctr+=1
                dfs(city)

        return ctr


        #sol 1: O(n^2) time & O(n^2) space

        adjs=defaultdict(list)
        seen=set()
        rows,cols=len(mat),len(mat[0])

        def dfs(node): #O(V+E) = O(n^2) time -> E≤n^2
            seen.add(node)
            for neighbor in adjs[node]:
                if neighbor not in seen:
                    dfs(neighbor)

        for i in range(rows): #O(n^2) time
            for j in range(i+1,cols):
                if mat[i][j]==1:
                    adjs[i].append(j)
                    adjs[j].append(i)

        
        ctr=0
        for i in range(rows):
            if i not in seen:
                ctr+=1
                dfs(i)

        return ctr
