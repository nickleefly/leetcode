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

    def twoPointers(self, nums1: List[int], nums2: List[int]) -> float:
        # Get the lengths of the input arrays nums1 and nums2
        m, n = len(nums1), len(nums2)
        # Calculate the position of the median in the merged sorted array
        mid = (m + n) // 2 + 1
        # Initialize two variables to keep track of the previous two largest elements
        prev2 = prev1 = None
        # Initialize two index variables for nums1 and nums2
        i = j = 0

        # Merge nums1 and nums2 while keeping track of the two previous largest elements
        for _ in range(mid):
            prev2 = prev1
            if j == n or (i != m and nums1[i] <= nums2[j]):
                prev1 = nums1[i]
                i += 1
            else:
                prev1 = nums2[j]
                j += 1

        # Calculate and return the median of the merged sorted array
        return prev1 if (m + n) % 2 else (prev1 + prev2) / 2

    def binarySearch(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure that nums1 is the smaller array to simplify the algorithms
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_length = m + n

        # Binary search for the partition point where nums1 and nums2 are divided
        left, right = 0, m
        while left <= right:
            # Define the partition points for nums1 and nums2
            i = (left + right) // 2
            j = (total_length + 1) // 2 - i

            # Check if the partition is correct
            if i < m and nums1[i] < nums2[j - 1]:
                left = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                # The partition is correct, calculate the median
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if total_length % 2 == 1:
                    return max_left

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2.0


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))
