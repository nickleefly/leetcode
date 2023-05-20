def maxSubArray(nums):
    # Initialize max_ending_here and max_so_far to the first element of the array.
    max_ending_here = max_so_far = nums[0]

    # Iterate over the rest of the elements in the array.
    for i in range(1, len(nums)):
        # Update max_ending_here to be the maximum of the current element and the sum of the current element and max_ending_here.
        max_ending_here = max(nums[i], max_ending_here + nums[i])

        # Update max_so_far to be the maximum of max_so_far and max_ending_here.
        max_so_far = max(max_so_far, max_ending_here)

    # Return max_so_far.
    return max_so_far


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))

"""
The algorithm works by maintaining two variables: max_ending_here and max_so_far. max_ending_here
stores the maximum sum of any subarray ending at the current element, and max_so_far stores the
maximum sum of any subarray in the entire array.

At each step, we update max_ending_here to be the maximum of the current element and the sum of the
current element and max_ending_here. We then update max_so_far to be the maximum of max_so_far and
max_ending_here.

At the end of the loop, max_so_far will store the maximum sum of any subarray in the array.
"""
