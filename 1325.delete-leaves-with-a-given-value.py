#
# @lc app=leetcode id=1325 lang=python3
#
# [1325] Delete Leaves With a Given Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root.left is None and root.right is None and root.val == target:
            return root
        
        def dfs(node):
            if node.left==None and node.right==None:
                if node.val==target:
                    return True
                return False
            
            left=right=False
            
            if node.left:
                left=dfs(node.left)
            if node.right:
                right=dfs(node.right)
                
            if left:
                node.left = None
            
            if right:
                node.right = None
            
            if not node.left and not node.right:
                if node.val == target:
                    return True
                return False
        
        dfs(root)
        if not root.left and not root.right:
            if root.val == target:
                root=None
        return root
# @lc code=end

