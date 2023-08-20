class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        x, y = len(maze), len(maze[0])
        q.append([entrance[0], entrance[1], 0])
        ans = float('inf')
        seen = set()
        while len(q):
            s = len(q)

            for i in range(s):
                r, c, v = q.popleft()
                if maze[r][c] == "." and (r,c) not in seen:
                    if (
                        [r, c] != entrance
                        and (not r
                        or not c
                        or r == x-1
                        or c == y-1)
                    ):
                        return v
                    v += 1
                    seen.add((r,c))
                    if r + 1 < x and maze[r + 1][c] == ".":
                        q.append([r + 1, c, v])
                    if r - 1 >= 0 and maze[r-1][c] == '.':
                        q.append([r-1,c,v])
                    if c+1 < y and maze[r][c+1] == '.':
                        q.append([r,c+1,v])
                    if c-1 >= 0 and maze[r][c-1] == '.':
                        q.append([r,c-1,v])

        return ans if ans != float('inf') else -1
