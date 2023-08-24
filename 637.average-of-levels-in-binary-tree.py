#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def bfs(root):
            ans=[]
            
            q=deque([root])
            
            while q:
                s=len(q)
                curr=0
                for _ in range(s):
                    node=q.popleft()
                    curr+=node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                ans.append(curr/s)
            return ans
        return bfs(root)
# @lc code=end

