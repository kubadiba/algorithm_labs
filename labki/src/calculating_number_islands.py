class IslandCounter:
    def __init__(self, row, col, g):
        self.col = col
        self.row = row
        self.graph = g

    def is_safe(self, i, j, visited):
        return (
            0 <= i < self.row
            and 0 <= j < self.col
            and not visited[i][j]
            and self.graph[i][j]
        )

    def dfs(self, i, j, visited):
        row_num = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_num = [-1, 0, 1, -1, 1, -1, 0, 1]

        queue = [(i, j)]

        while queue:
            x, y = queue.pop(0)
            visited[x][y] = True

            for k in range(8):
                if self.is_safe(x + row_num[k], y + col_num[k], visited):
                    queue.append((x + row_num[k], y + col_num[k]))

    def count_islands(self):
        visited = [[False for j in range(self.col)] for i in range(self.row)]

        count = 0
        for i in range(self.row):
            for j in range(self.col):
                if visited[i][j] is False and self.graph[i][j] == 1:
                    self.dfs(i, j, visited)
                    count += 1

        return count
