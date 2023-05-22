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

    def longestPalindromManacher(self, s: str) -> str:
        # Inserting separator character ^ between each character
        n = len(s)
        t = '#' + '#'.join(s) + '#'
        n_t = len(t)

        # Initializing two arrays P and C which will store information about each palindrome
        P = [0] * n_t
        C = R = 0

        # Loop for each character in string t
        for i in range(n_t):
            # Calculate mirror index (j)
            j = 2 * C - i
            # Check if we can expand palindrome centered at i
            if i < R:
                P[i] = min(R - i, P[j])

            # Expand palindrom centered at i
            while i + P[i] + 1 < n_t and i - P[i] - 1 >= 0 and t[i + P[i] + 1] == t[i - P[i] - 1]:
                P[i] += 1

            # Update center and right boundary of current palindrome
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Retrieve the longest palindrome
        max_len, center_index = max((len_t, i) for i, len_t in enumerate(P))
        start = (center_index - max_len) // 2
        end = start + max_len - 1

        return s[start:end + 1]
