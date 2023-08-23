#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        elif bool(root.left) ^ bool(root.right):
            return False
        def bfs(node):
            q = deque([node])
            while q:
                size = len(q)
                if size>1:
                    if size%2!=0:
                        return False
                    for i in range(floor(size/2)):
                        print(q[i] if q[i] == None else q[i].val, q[size-i-1] if q[size-i-1] == None else q[size-i-1].val)
                        if q[i]==None and q[size-i-1]!=None:
                            return False
                        elif q[i]!=None and q[size-i-1]==None:
                            return False
                        elif q[i]!=None and q[size-i-1]!=None and q[i].val != q[size-i-1].val:
                            return False
                for i in range(size):
                    node = q.popleft()
                    if node:
                        q.append(node.left)
                        q.append(node.right)
            return True
        def recurse(node, side=None):
            if not node.left and not node.right:
                return [node.val]
            left=[None]
            right=[None]
            if node.left:
                left=recurse(node.left,side)
            if node.right:
                right=recurse(node.right,side)
            return left+right+[node.val] if side=='left' else right+left+[node.val]
        
        def dfs(root):
            return recurse(root.left,'left') == recurse(root.right,'right')
        
        return dfs(root) and bfs(root)
# @lc code=end

