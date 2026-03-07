#
# Problem: 1202. Smallest String With Swaps
# Difficulty: Medium
# Link: https://leetcode.com/problems/smallest-string-with-swaps/
# Language: python3
# Date: 2026-03-07


#try bfs

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
    
        #sol 1: O(n+m+nlogn) time & O(n+m) space

        def dfs(node): #O(n+m) time & O(n) space
            seen.add(node)
            component.append(node)
            for neighbor in adjs[node]:
                if neighbor not in seen:
                    dfs(neighbor)
        

        adjs=defaultdict(list)
        for u,v in pairs: #O(m) time & O(m) space
            adjs[u].append(v)
            adjs[v].append(u)
        
        s=list(s)
        seen=set()

        for i in range(len(s)):
            if i not in seen:

                component=[]
                dfs(i)

                chars=[s[i] for i in component]
                chars.sort() #O(nlogn) time
                component.sort()

                for i,ch in zip(component,chars):
                    s[i]=ch


        return "".join(s)
