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

        """
        The Manacher's algorithm has a time complexity of O(n).

        In this implementation, first we insert a separator character ^ between every two consecutive characters in the input string, this helps us to have only one type of palindromes (odd length), because when we expand around each center, we will have either odd length or even length palindrome in one iteration, it is simpler to just deal with odd length palindromes only.

        We initialize two arrays, P and C. When we are expanding our palindrome, P[i] will store the length of the longest palindrome centered on i. C is our center (or centers) of the current longest palindrome discovered so far, and R measures the right boundary of that palindrome. At each i, we check whether i is within the range [2C−i, R] (which is the palindrome range) or i is outside that range. If i is outside our range, we need to start with one-character palindrome, but if i is within that range, there are three possibilities:

        Case 1: if the palindrome j has left and right boundaries strictly inside the palindrome centered at C, then palindrome at j is also a palindrome centered at i. Set P[i] to that value.

        Case 2: if the right edge of the palindrome at j is outside the right edge of the palindrome centered at i, then P[i] can simply be set to the length of the palindrome at j. Then we check whether the palindrome can be further extended or not.

        Case 3: if the palindrome at j hits or exceeds the border of the palindrome centered at i, then we can’t expand this palindrome without going past the right border. So, we stop expanding at that point.

        We also need to keep track of the center and right boundary of the palindrome that we have expanded so far, this is used to determine whether we have to expand our current palindrome or we can simply set P[i] to the length of the palindrome at j.

        Finally, we just need to retrieve the longest palindrome from P and convert it back into the actual substring of s.
        """