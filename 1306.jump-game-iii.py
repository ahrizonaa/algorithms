#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        n = len(arr)

        seen = set()
        q = deque([start])

        while q:
            node = q.popleft()
            
            if arr[node] == 0:
                return True
            
            if node not in seen:
                seen.add(node)
                jumpright = node + arr[node]
                jumpleft = node - arr[node]
                if jumpright < n and jumpright not in seen:
                    q.append(jumpright)
                if jumpleft >= 0 and jumpleft not in seen:
                    q.append(jumpleft)

        return False


# @lc code=end

