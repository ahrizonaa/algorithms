#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        def decrement(x):
            return (x - 1) % 10
        
        def increment(x):
            return (x + 1) % 10
        
        def neighbors(node):
            vertices = []
            nums = list(node)
            for i in range(len(nums)):
                up = str(increment(int(nums[i])))
                down = str(decrement(int(nums[i])))
                vertices.append(nums[0:i]+[up]+nums[i+1:])
                vertices.append(nums[0:i]+[down]+nums[i+1:])
            return ["".join(arr) for arr in vertices]                   
        
        root = [('0000', 0)]
        q = deque(root)
        seen = set(deadends+['0000'])
        while q:
            node = q.popleft()
            if node[0] == target:
                return node[1]
            for neighbor in neighbors(node[0]):
                if neighbor == target:
                    return node[1]+1
                if neighbor not in seen:
                    q.append((neighbor,node[1]+1))
                    seen.add(neighbor)

        return -1
# @lc code=end
