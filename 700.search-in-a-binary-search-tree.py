#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            if node.val==val:
                return node
            
            if val < node.val:
                return dfs(node.left)
            return dfs(node.right)
        
        return dfs(root)
# @lc code=end

