class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        nn = n * n
        if nn <= 6:
            return 1
        nodes = [None] * (nn + 1)
        steps = [-1] * (nn + 1)
        node = 1
        for row in range(n - 1, -1, -1):
            start = stop = step = 0
            if (n % 2 == 0 and row % 2 == 0) or (n % 2 != 0 and row % 2 != 0):
                start, stop, step = n - 1, -1, -1
            else:
                start, stop, step = 0, n, 1
            for col in range(start, stop, step):
                nodes[node] = [row, col]
                node += 1

        q = deque([1])
        steps[1] = 0

        while len(q):
            node = q.popleft()
            for i in range(node + 1, min(node + 6, nn) + 1):
                row, col = nodes[i]
                dest = None
                if board[row][col] != -1:
                    dest = board[row][col]
                else:
                    dest = i
                if steps[dest] == -1:
                    steps[dest] = steps[node] + 1
                    q.append(dest)

        return steps[nn]