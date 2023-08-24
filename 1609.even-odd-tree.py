#
# @lc app=leetcode id=1609 lang=python3
#
# [1609] Even Odd Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        def bfs(root):
            
            q=deque([root])
            depth=0
            while q:
                s=len(q)
                prev=None
                for _ in range(s):
                    node=q.popleft()
                    if depth%2==0:
                        if node.val%2==0 or prev!=None and prev>=node.val:
                            return False
                        prev=node.val
                    else:
                        if node.val%2!=0 or prev!=None and prev<=node.val:
                            return False
                        prev=node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                depth+=1
                            
            return True
        
        return bfs(root)
# @lc code=end

