from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        intersect = set()

        for num in nums2:
            if num in set1:
                intersect.add(num)

        return list(intersect)

    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        for num in nums1:
            nums1_dict[num] = nums1_dict.get(num, 0) + 1

        intersect = []
        for num in nums2:
            if num in nums1_dict and nums1_dict[num] > 0:
                intersect.append(num)
                nums1_dict[num] -= 1
                if nums1_dict[num] == 0:
                    del nums1_dict[num]

        return intersect


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(Solution().intersection1(nums1, nums2))
