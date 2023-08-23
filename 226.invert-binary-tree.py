#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root):
            if not root:
                return root
            q = deque([root])
            while q:
                node = q.popleft()
                tmp = node.left
                node.left = node.right
                node.right = tmp
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            return root
        
        return bfs(root)
# @lc code=end

