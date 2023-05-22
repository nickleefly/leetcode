from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        pacific, atlantic = set(), set()

        def dfs(i: int, j: int, visited: set) -> None:
            visited.add((i, j))
            for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= r < m and 0 <= c < n and matrix[r][c] >= matrix[i][j] and (r, c) not in visited:
                    dfs(r, c, visited)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)

        for j in range(n):
            dfs(0, j, pacific)
            dfs(m-1, j, atlantic)

        return list(pacific & atlantic)
