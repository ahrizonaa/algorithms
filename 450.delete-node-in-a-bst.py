#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def predecessor(self,node):
        if node.right:
            return self.predecessor(node.right)
        return node.val

    def successor(self,node):
        if node.left:
            return self.successor(node.left)
        return node.val
    
    def deleteNode(self, root, key: int):

        if not root:
            return None
        
        if key==root.val:
            if not root.right and not root.left:
                root=None
            elif root.right:
                root.val=self.successor(root.right)
                root.right=self.deleteNode(root.right,root.val)
            else:
                root.val=self.predecessor(root.left)
                root.left=self.deleteNode(root.left,root.val)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)     
            
        return root       
# @lc code=end