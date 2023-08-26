#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph=defaultdict(list)
        
        for truster,trustee in trust:
            graph[truster].append(trustee)
        
        
        if n - len(graph) != 1:
            return -1
        
        judge=None
        for person in range(1,n+1):
            if person not in graph:
                judge=person
                break
        
        for person in graph:
            if judge not in graph[person]:
                return -1
            
        return judge
# @lc code=end

