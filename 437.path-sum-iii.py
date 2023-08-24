#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        ans_pre: int = 0
        ans_post: int = 0
        def dfs_preorder(node: TreeNode, sums: List[int]) -> bool:
            nonlocal ans_pre
            sums.append(0)
            for i in range(len(sums)):
                sums[i]+=node.val
                if sums[i]==targetSum: ans_pre+=1
            
            
            if node.left:
                dfs_preorder(node.left, sums)
            if node.right:
                dfs_preorder(node.right, sums)
            
            sums.pop(-1)
            
            for i in range(len(sums)):
                sums[i]-=node.val
                
        def dfs_postorder(node: TreeNode) -> List[int]:
            nonlocal ans_post
            sums = [0]
            if node.left:
                sums.extend(dfs_postorder(node.left))
            if node.right:
                sums.extend(dfs_postorder(node.right))
            
            for i in range(len(sums)):
                sums[i]+=node.val
                if sums[i]==targetSum:
                    ans_post+=1
            return sums
        
        # demonstrating preorder and postorder traversal
        dfs_preorder(root,[])
        dfs_postorder(root)
        return ans_pre and ans_post
# @lc code=end

