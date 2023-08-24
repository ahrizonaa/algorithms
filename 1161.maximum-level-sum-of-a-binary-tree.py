#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root):
            depth=1
            ans=1
            q=deque([root])
            
            maxx=float('-inf')
            while q:
                s=len(q)
                curr=0
                for _ in range(s):
                    node=q.popleft()
                    curr+=node.val
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                if curr>maxx:
                    ans=depth
                    maxx=curr
                depth+=1
            return ans
        return bfs(root)
# @lc code=end

