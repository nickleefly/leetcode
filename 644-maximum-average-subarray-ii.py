from typing import List


class Solution:
    def maxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        max_avg = total / k

        start = 0
        # we iterate through the array from index k to the end
        for end in range(k, len(nums)):
            # In each iteration, we remove the element at start from the
            # total and add the new element at end
            total += nums[end] - nums[start]
            max_avg = max(max_avg, total / k)
            # We increment start to slide the window
            start += 1

        return max_avg


nums = [1, 12, -5, -6, 50, 3]
k = 3
print(Solution().maxAverage(nums, k))
