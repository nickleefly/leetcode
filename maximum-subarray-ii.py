def max_subarray_ii(nums):
    """
    Finds the maximum subarray sum in an array, where the subarray can have non-contiguous elements.

    Args:
      nums: An array of integers.

    Returns:
      The maximum subarray sum.
    """

    max_ending_here = max_so_far = nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)
        dp[i] = max_ending_here

    return max_so_far


"""
The algorithm works by maintaining two variables: max_ending_here and max_so_far. max_ending_here
stores the maximum sum of any subarray ending at the current element, and max_so_far stores the
maximum sum of any subarray in the entire array.

At each step, we update max_ending_here to be the maximum of the current element and the sum of the
current element and max_ending_here. We then update max_so_far to be the maximum of max_so_far and
max_ending_here.

At the end of the loop, max_so_far will store the maximum sum of any subarray in the array.

The dp array is used to store the maximum sum of any subarray ending at each index. This allows us to
update max_ending_here more quickly.
"""

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_subarray_ii(nums))
