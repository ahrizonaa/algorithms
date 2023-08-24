#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root,0,'r')
        return self.ans

    def dfs(self,node,curr,prev) -> None:
        self.ans = max(curr,self.ans)
        if node.left:
            if prev=='r':
                self.dfs(node.left,curr+1,'l')
            else:
                self.dfs(node.left,1,'l')
        if node.right:
            if prev=='l':
                self.dfs(node.right,curr+1,'r')
            else:
                self.dfs(node.right,1,'r')
        
# @lc code=end