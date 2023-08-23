#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q:
            return True
        
        def dfs(p,q):
            if p == None and q == None:
                return True
            return p and q and p.val == q.val and dfs(p.left,q.left) and dfs(p.right,q.right)
        
        return dfs(p,q)
# @lc code=end

