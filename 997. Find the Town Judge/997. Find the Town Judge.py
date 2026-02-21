#
# Problem: 997. Find the Town Judge
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-town-judge/description/
# Language: python3
# Date: 2026-02-21


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        #sol 1: O(n) time & O(n) space

        #building adjacency list
        adj={i:[] for i in range(1,n+1)}
        for u,v in trust:
            adj[u].append(v)

        #find candidate judge
        judge=-1
        for person in range(1,n+1):
            if len(adj[person])==0:
                judge=person
                break

        if judge==-1:
            return -1

        #checking all trusts the judge
        for person in (p for p in range(1,n+1) if p!=judge): #generator experssion (same cost)
            # if person==judge:
            #     continue
            if judge not in adj[person]:
                return -1

        return judge
