#
# Problem: 690. Employee Importance
# Difficulty: Medium
# Link: https://leetcode.com/problems/employee-importance/
# Language: python3
# Date: 2026-02-21


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        #sol 2: O(n) time & O(n) space

        empMap = {emp.id:emp for emp in employees}

        def dfs(node):
            return node.importance + \
            sum(dfs(empMap[neighbor]) for neighbor in node.subordinates)

        return dfs(empMap[id])



        #sol 1: O(n) time & O(n) space

        empMap={emp.id:emp for emp in employees}

        def dfs(id):
            currEmp=empMap[id]
            summ=currEmp.importance

            for neighbor in currEmp.subordinates:
                summ+=dfs(neighbor)

            return summ

        return dfs(id)
