from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum < abs(target) or (total_sum + target) % 2 != 0:
            return 0
        subset_sum = (total_sum + target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for i in range(n):
            for j in range(subset_sum, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]

        return dp[subset_sum]
