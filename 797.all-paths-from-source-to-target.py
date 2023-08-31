#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#


# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)

        for i, row in enumerate(graph[:-1]):
            g[i] = row

        start, end = 0, len(graph) - 1

        paths = []

        def bfs(node):
            nonlocal paths

            q = deque([[node]])

            while len(q) != 0:
                num = len(q)
                for i in range(num):
                    first = q.popleft()
                    if first[-1] == end:
                        paths.append(first)
                    else:
                        for person in g[first[-1]]:
                            q.append(first + [person])

        bfs(start)
        return paths


# @lc code=end
