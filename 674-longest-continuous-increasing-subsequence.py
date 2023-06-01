class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        start = 0
        max_len = 1
        for end in range(1, len(nums)):
            if nums[end] > nums[end - 1]:
                max_len = max(max_len, end - start + 1)
            else:
                start = end

        return max_len
