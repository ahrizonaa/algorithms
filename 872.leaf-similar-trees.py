#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node.left == None and node.right == None:
                return [node.val]
            leaves = []
            if node.left:
                leaves.extend(dfs(node.left))
            if node.right:
                leaves.extend(dfs(node.right))
            return leaves
        
        return dfs(root1) == dfs(root2)
# @lc code=end

