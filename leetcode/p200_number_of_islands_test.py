from typing import List


class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = None
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        islands = 0
        r = 0
        while r < rows:
            c = 0
            while c < cols:
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
                grid[r][c] = None
                c += 1
            r += 1

        return islands

    def numIslands2(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def points():
            for r in range(rows):
                for c in range(cols):
                    yield (r, c)

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = None
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        islands = 0
        for r, c in points():
            if grid[r][c] == '1':
                dfs(r, c)
                islands += 1
            grid[r][c] = None
        return islands

    def numIslands3(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def valid(r: int, c: int) -> bool:
            return 0 <= r and r < rows and 0 <= c and c < cols

        def neighbors(r: int, c: int):
            if valid(r-1, c):
                yield (r-1, c)
            if valid(r+1, c):
                yield (r+1, c)
            if valid(r, c-1):
                yield (r, c-1)
            if valid(r, c+1):
                yield (r, c+1)
        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited:
                    continue
                if grid[r][c] == '0':
                    visited.add((r, c))
                else:
                    # Flood-Fill
                    islands += 1
                    queue = [(r, c)]
                    while len(queue) > 0:
                        r2, c2 = queue.pop()
                        if (r2, c2) in visited or grid[r2][c2] != '1':
                            continue
                        visited.add((r2, c2))
                        for p in neighbors(r2, c2):
                            queue.append(p)
        return islands


def test_num_islands():
    s = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert s.numIslands(grid) == 1
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert s.numIslands(grid) == 3
