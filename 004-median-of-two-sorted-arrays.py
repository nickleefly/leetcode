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
    """
    The idea is to first merge the two sorted arrays into a single sorted array, which can be done
    efficiently in O(n) time using the + operator and the sort() method. Then, we can calculate
    the median index based on the length of the merged array. Finally, we check if the number of
    elements is odd or even and return the median accordingly. The time complexity of this solution
    is O(n log n) due to the use of sort(), but it can be improved to O(n) using a more involved
    algorithm such as binary search.
    """

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
        """
        The two-pointer approach in this implementation merges two sorted arrays nums1 and nums2
        and finds the median of the merged sorted array in a single pass using two pointers i and j.
        Here's how it works:

        First, the lengths of the two input arrays are calculated. Then, the position of the median
        in the merged sorted array is calculated as mid = (m + n) // 2 + 1.

        Two variables prev2 and prev1 are initialized to keep track of the previous two largest elements.
        Two index variables i and j are also initialized to keep track of the current positions in nums1
        and nums2, respectively.

        Next, a loop is executed mid times to merge nums1 and nums2 into a single sorted array while
        keeping track of the two previous largest elements. At each iteration, the loop checks if the
        current element in nums1 is smaller than or equal to the current element in nums2. If it is,
        the current element in nums1 is added to the merged sorted array and i is incremented.
        Otherwise, the current element in nums2 is added to the merged sorted array and j is incremented.

        After the loop is completed, the median of the merged sorted array is calculated and returned.
        If the total length of nums1 and nums2 is odd, the median is the middle element of the merged
        sorted array, which is prev1. If the total length is even, the median is the average of the
        middle two elements, which are prev1 and prev2.

        Overall, this implementation has a time complexity of O(m + n) due to the single pass of merging two
        sorted arrays. The space complexity of this implementation is O(1) since we don't use any extra data
        structure to store the merged sorted array.
        """

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
    """
    The idea behind this binary search solution is to divide both arrays into two parts left and right,
    such that the number of elements in the left part is equal to the number of elements in the right
    part (or differs by one if the total number of elements is odd). The median is then the average of
    the maximum element in the left part and the minimum element in the right part.

    The algorithm starts by considering the smaller array nums1 as the left part and the larger array
    nums2 as the right part. It then performs a binary search on the left part to find the partition
    point i such that nums1[0:i] and nums2[0:j] are the left parts, and nums1[i:m] and nums2[j:n] are
    the right parts.

    At each iteration, the algorithm calculates the partition point i and its corresponding j, and
    checks if the partition is correct by comparing nums1[i] with nums2[j - 1] and nums1[i - 1] with
    nums2[j]. If the partition is correct, it calculates the median and returns it.

    The time complexity of this solution is O(log(min(m, n))), since each iteration of the binary
    search reduces the size of the left part by half. The space complexity is O(1).

    Note that the implementation above assumes that the input arrays are sorted in non-descending order.
    """


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))
