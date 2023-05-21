class Solution:
    def numSquares(self, n: int) -> int:
        # Initialize an array to store the minimum number of perfect
        # squares needed to sum to each integer from 0 to n
        min_num_squares = [float('inf')]*(n+1)
        min_num_squares[0] = 0

        # Iterate through all integers from 1 to n
        for i in range(1, n+1):
            # Find the minimum number of perfect squares needed to sum to i
            j = 1
            while j*j <= i:
                min_num_squares[i] = min(
                    min_num_squares[i], min_num_squares[i-j*j]+1)
                j += 1

        # Return the minimum number of perfect squares needed to sum to n
        return min_num_squares[n]

    def num_squares(self, n):
        # Create a list of all perfect squares less than or equal to n.
        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]

        # Create a table to store the minimum number of perfect squares needed to
        # reach each number.
        dp = [float('inf')]*(n+1)
        dp[0] = 0

        # Iterate over the squares, and for each square, update the table to store
        # the minimum number of perfect squares needed to reach that number.
        for square in squares:
            for i in range(square, n + 1):
                dp[i] = min(dp[i], dp[i - square] + 1)
                # print(f'i is {i} square is {square} dp is {dp}')

        return dp[-1]


print(Solution().num_squares(12))
