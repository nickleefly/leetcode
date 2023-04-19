class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # Initialize a table of boolean values to store the palindrome information of substrings
        dp = [[False for _ in range(n)] for _ in range(n)]

        # Initialize the longest and starting and ending indices of the palindrome substring
        longest, start, end = 1, 0, 0

        # Base case: all substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        # Case 1: check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                longest, start, end = 2, i, i + 1

        # Case 2: check for substrings of length >= 3
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > longest:
                        longest, start, end = length, i, j

        # Return the longest palindromic substring
        return s[start:end + 1]
    """
    The idea behind this dynamic programming solution is to use a table dp of boolean values
    to store the palindrome information of all substrings of s. We can fill this table using
    the following recurrence:

        dp[i][j] = True                   if i == j
        s[i] == s[j]                      if j == i + 1
        s[i] == s[j] && dp[i + 1][j - 1]  if j > i + 1
    The base case is that all substrings of length 1 are palindromes, which are stored in the
    diagonal entries of the table. For substrings of length 2, we check if they are palindromes
    by comparing the first and second characters. For substrings of length greater than 2,
    we check if they are palindromes by checking if the first and last characters are the same
    and the inside substring is also a palindrome.

    Once we have filled the table dp, we find the longest palindromic substring by iterating over all
    substrings s[i:j+1] and finding the one with the longest length that is also a palindrome. We can
    keep track of the longest palindrome substring seen so far and its starting and ending indices.

    The time complexity of this solution is O(n^2) since we fill a table of size n x n. The space complexity
    is also O(n^2) since we need to store the table of boolean values. Note that we can further optimize the
    space complexity to O(n) by using two vectors instead of a matrix to represent the current and previous
    rows of the dynamic programming table.
    """