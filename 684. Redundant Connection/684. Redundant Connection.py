#
# Problem: 684. Redundant Connection
# Difficulty: Medium
# Link: https://leetcode.com/problems/redundant-connection/
# Language: python3
# Date: 2026-03-07


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        #sol 1: O(n^2) time & O(n) space

        adjs=defaultdict(list)

        def dfsValidPath(node,target,seen): #O(n) time
            #base case
            if target in adjs[node]: return True

            # #base case
            # if node==target: return True

            seen.add(node)

            for neighbor in adjs[node]:
                if neighbor not in seen and dfsValidPath(neighbor,target,seen):
                    return True

            return False

        for u,v in edges:
            if u in adjs and v in adjs and dfsValidPath(u,v,set()): #O(n) time
                return [u,v]

            adjs[u].append(v)
            adjs[v].append(u)

        return None
