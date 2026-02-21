#
# Problem: 1791. Find Center of Star Graph
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-center-of-star-graph/submissions/1926462568/
# Language: python3
# Date: 2026-02-21


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        adj={}
        for u,v in edges:
            adj.setdefault(u,[]).append(v)
            adj.setdefault(v,[]).append(u)

            # if u not in adj:
            #     adj[u]=[]
            # if v not in adj:
            #     adj[v]=[]
            # adj[u].append(v)
            # adj[v].append(u)

        for node in adj:
            if len(adj[node])>1:
                return node


        #sol 2: O(1) time & O(1) space

        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


        #sol 1: O(1) time & O(1) space

        a,b=edges[0]
        c,d=edges[1]

        if a==c or a==d:
            return a
        return b
