def unique_paths(m, n):
    """
    Finds the number of unique paths that a robot can take to reach the bottom-right corner of a grid.

    Args:
      m: The number of rows in the grid.
      n: The number of columns in the grid.

    Returns:
      The number of unique paths.
    """

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]

    return dp[-1][-1]


m = 3
n = 7

print(unique_paths(m, n))

"""
The algorithm works by building a table of the number of unique paths that can be taken to reach each
cell in the grid. The table is initialized with a 1 in the top-left corner, and then each cell is
filled in by adding the number of paths that can be taken to reach the cell from the top and left
cells. The number of unique paths to the bottom-right corner is then the value in the bottom-right
cell of the table.
"""
