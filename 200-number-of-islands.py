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
