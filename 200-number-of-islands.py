class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col):
            # Check if the current cell is within the grid and is part of an island
            if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0'):
                return

            # Mark the current cell as visited by changing its value to '0'
            grid[row][col] = '0'

            # Recursively search the adjacent cells to find all the cells that are part of the same island
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        # Check if the input grid is empty or None
        if not grid:
            return 0

        # Initialize the island counter to 0
        island_count = 0

        # Iterate through each cell in the input grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # If the current cell is part of an unvisited island, increment the island counter and search
                # all adjacent cells to find all the cells that are part of the same island
                if grid[row][col] == '1':
                    island_count += 1
                    dfs(row, col)

        # Return the number of islands
        return island_count


"""
The `numIslands` function takes in a 2D grid of `m` rows and `n` columns and
returns the number of islands in the grid. An island is represented by a group
of connected `1`s that are surrounded by `0`s.

The function starts by defining a `dfs` function that performs a depth-first
search to find all the cells that are part of the same island. The `dfs` function
takes in the row `row` and column `col` of the current cell.

The `dfs` function first checks if the current cell is within the grid and is part
of an island. If the current cell is not part of an island, the function simply returns.
Otherwise, the function marks the current cell as visited by changing its value to `'0'`
and recursively searches all adjacent cells to find all the cells that are part of the
same island.

The `numIslands` function checks if the input grid is empty or `None`. If the grid is
empty or `None`, the function returns `0`. Otherwise, it initializes the island
counter `island_count` to `0`.

The function then iterates through each cell in the input grid. If the current
cell is part of an unvisited island, the function increments the island counter
and searches all adjacent cells to find all the cells that are part of the same island.

Once it has searched all the cells in the grid, the function returns the number of islands.
"""
