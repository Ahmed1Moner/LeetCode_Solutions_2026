#
# Problem: 1202. Smallest String With Swaps
# Difficulty: Medium
# Link: https://leetcode.com/problems/smallest-string-with-swaps/description/
# Language: python3
# Date: 2026-03-06


#try bfs

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        def dfs(node):
            seen.add(node)
            component.append(node)
            for neighbor in adjs[node]:
                if neighbor not in seen:
                    dfs(neighbor)
        

        adjs=defaultdict(list)
        for u,v in pairs:
            adjs[u].append(v)
            adjs[v].append(u)
        
        s=list(s)
        seen=set()

        for i in range(len(s)):
            if i not in seen:

                component=[]
                dfs(i)

                chars=[s[i] for i in component]
                chars.sort()
                component.sort()

                for i,ch in zip(component,chars):
                    s[i]=ch


        return "".join(s)
