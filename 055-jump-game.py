def can_jump(nums):
    # Initialize farthest to 0.
    farthest = 0

    # Iterate over the rest of the elements in the array.
    for i in range(len(nums)):

        # If i is greater than farthest, then it is not possible to reach the last index.
        if i > farthest:
            return False

        # Update farthest to be the maximum of farthest and i + nums[i].
        farthest = max(farthest, i + nums[i])

    # If farthest is equal to the length of the array, then it is possible to reach the last index.
    return farthest == len(nums)
