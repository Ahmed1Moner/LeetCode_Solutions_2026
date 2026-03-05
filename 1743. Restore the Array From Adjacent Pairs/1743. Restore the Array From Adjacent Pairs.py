#
# Problem: 1743. Restore the Array From Adjacent Pairs
# Difficulty: Medium
# Link: https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
# Language: python3
# Date: 2026-03-05


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        #sol 1: O(n) time & O(n) space

        def dfs(num): #O(n) time
            seen.add(num)
            for nxtNum in adjs[num]:
                if nxtNum in seen: continue
                dfs(nxtNum)
            ans.append(num)
        

        #build the graph
        adjs=defaultdict(list) #O(n) space
        for u,v in adjacentPairs: #O(n) time
            adjs[u].append(v)
            adjs[v].append(u)

        start=None
        for node,neighbor in adjs.items(): #O(n) time
            #find an endpoint: 1 degree node
            if len(neighbor)==1:
                start=node
                break
        
        seen,ans=set(),[]
        dfs(start)
        return ans
