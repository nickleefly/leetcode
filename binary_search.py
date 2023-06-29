def binary_search(self, nums, target):
    # corner case
    if not nums:
        return -1

    start, end = 0, len(nums) - 1
    """
    use start + 1 < end not start < end is to avoid dead loop
    no dead loop in first position of target
    but dead loop in last position of target
    eg nums=[1, 1,] target 1
    """
    while start + 1 < end:
        mid = (start + end) // 2

        if nums[mid] < target:
            start = mid
        elif nums[mid] == target:
            end = mid
        else:
            end = mid
    """
    the condiction for loop above is start + 1 < end
    after loop is over, we need to check if start and end are next to each other
    eg(1 and 2, 3 and 4) if we are looking for first position of target, then we
    check start first, or will use end
    """
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1
