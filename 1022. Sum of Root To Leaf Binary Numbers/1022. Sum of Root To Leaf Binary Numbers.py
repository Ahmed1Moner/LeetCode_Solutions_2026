#
# Problem: 1022. Sum of Root To Leaf Binary Numbers
# Difficulty: Easy
# Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/?envType=daily-question&envId=2026-02-24
# Language: python3
# Date: 2026-02-24


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        #sol 2: O(n) time & O(h) space -> h:height->balanced(logn)

        def dfs(node,path):
            #base case 1
            if not node: #missing child
                return 0

            path=path*2+node.val

            #base case 2
            if not node.left and not node.right:
                return path

            x=dfs(node.left,path)
            y=dfs(node.right,path)
            return x+y


        return dfs(root,0)


        #sol 1: O(n.l) time & O(h) space -> l:len(path) & h:height->balanced(logn)

        def dfs(node,path):
            if not node:
                return 0
            
            path+=str(node.val) #O(l)

            if not node.left and not node.right:
                return int(path,2)

            return dfs(node.left,path) + dfs(node.right,path)

        
        return dfs(root,'')
