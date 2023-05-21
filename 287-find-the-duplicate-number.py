def findDuplicate(nums):
    # Initialize two pointers, slow and fast, to the first element
    # of the array
    slow = nums[0]
    fast = nums[0]

    # Move the slow pointer one step and the fast pointer two steps
    # at a time until they meet
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Reset the slow pointer to the first element of the array and move
    # both pointers at the same speed until they meet again
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    # Return the meeting point of the two pointers, which is the duplicate number
    return slow


nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))
