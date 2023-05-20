class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == '':
            return 0
        counter = 0  # max length of substring
        start = 0  # index where all the char between the start and i are all unique
        mark = {}  # all the char index we last seen

        for i in range(len(s)):
            char_now = s[i]
            if char_now in mark:
                start = max(start, mark[char_now]+1)
            counter = max(counter, i-start+1)
            mark[char_now] = i

        return counter


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
