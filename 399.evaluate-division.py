#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        answers = [-1]*len(queries)

        for i,(x,y) in enumerate(equations):
            val = {}
            val[y] = values[i]
            graph[x] += [val]
            rev = {}
            rev[x] = 1 / values[i]
            graph[y] += [rev]

        for node in graph: print(node,graph[node])
        
        q = deque()

        for i,query in enumerate(queries):
            multiplier = 1
            q = deque([(query,multiplier)])
            seen = set()
            # bfs
            while q:
                (numerator,denominator),multiplier = q.popleft()
                if numerator not in seen:
                    seen.add(numerator)
                    for neighboring_node in graph[numerator]:
                        node = list(neighboring_node.keys())[0]
                        ratio = neighboring_node[node]
                        if node == denominator:
                            answers[i] = multiplier * ratio
                            q.clear()
                            break
                        q.append(([node,denominator],multiplier*ratio))
        return answers
# @lc code=end