import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        k_pairs = []
        seen = set()

        # add the pair (0, 0) to the heap
        heapq.heappush(k_pairs, (nums1[0] + nums2[0], 0, 0))
        seen.add((0, 0))

        res = []
        while k_pairs and len(res) < k:
            # get the pair with the smallest sum from the heap
            _, i, j = heapq.heappop(k_pairs)
            res.append([nums1[i], nums2[j]])

            # add the next pairs to the heap
            if i + 1 < len(nums1) and (i + 1, j) not in seen:
                seen.add((i + 1, j))
                heapq.heappush(k_pairs, (nums1[i + 1] + nums2[j], i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in seen:
                seen.add((i, j + 1))
                heapq.heappush(k_pairs, (nums1[i] + nums2[j + 1], i, j + 1))

        return res
