class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create a set of all the words in the word dictionary for fast lookup
        word_set = set(wordDict)

        # Create a boolean list of length n+1, where n is the length of the input string s
        # dp[i] is True if s[0:i] can be segmented into words in the dictionary, False otherwise
        dp = [False] * (len(s) + 1)

        # An empty string can always be segmented into words in the dictionary
        dp[0] = True

        # Iterate through the input string s
        for i in range(1, len(s) + 1):
            # Iterate through all possible prefixes of s[0:i]
            for j in range(i):
                # If s[0:j] can be segmented into words in the dictionary and s[j:i] is also in the dictionary
                # then we can segment s[0:i] into words in the dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        # The last element of dp is True if s can be segmented into words in the dictionary
        return dp[-1]
