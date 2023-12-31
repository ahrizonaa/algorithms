#
# @lc app=leetcode id=1305 lang=python3
#
# [1305] All Elements in Two Binary Search Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return []
            return dfs(node.left)+[node.val]+dfs(node.right)
            
        return sorted(dfs(root1)+dfs(root2))
# @lc code=end

