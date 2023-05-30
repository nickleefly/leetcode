from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        d = defaultdict(int)
        d[0] = 1

        for n in nums:
            sums += n
            count += d[sums - k]
            d[sums] += 1

        return count


nums = [1, 1, 1]
k = 2
print(Solution().subarraySum(nums, k))
