from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two sorted arrays into a single sorted array
        merged = nums1 + nums2
        merged.sort()  # In-place sort

        # Calculate the median index (zero-indexed)
        n = len(merged)
        median_idx = n // 2  # Integer division

        # Check if the number of elements is odd or even
        if n % 2 == 0:
            # If even, return the average of the two middle elements
            return (merged[median_idx - 1] + merged[median_idx]) / 2
        else:
            # If odd, return the middle element
            return merged[median_idx]

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))