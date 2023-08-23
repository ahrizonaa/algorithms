#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == targetSum:
                return [[root.val]]
            return []
        
        def bfs(root):
            ans = []
            q = deque([(root,[])])
            while q:
                s = len(q)
                for _ in range(s):
                    node,currs = q.popleft()
                    currs = currs+ [node.val]
                    if node.left == None and node.right == None and sum(currs) == targetSum:
                        ans.append(currs)
                    if node.left:
                        q.append((node.left,currs))
                    if node.right:
                        q.append((node.right,currs))
            return ans
        
        ans = []
        stack = []
        def dfs(node):
            nonlocal stack
            nonlocal ans
            if not node.left and not node.right:
                if sum(stack)+node.val == targetSum:
                    ans.append(stack+[node.val])
                return
            
            stack.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            
            stack.pop()
        
        dfs(root)
        cmp = bfs(root)
        return ans if ans == cmp else cmp
# @lc code=end

