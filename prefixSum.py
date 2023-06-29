def minSubArrayLen1(nums, k):
    # prefix Sum -> prefix array index
    sum_to_index_map = dict()
    sum_to_index_map[0] = 0
    answer = float('inf')
    # prefix_sum is sum of numbers from start to a point
    prefix_sum = 0
    for i in range(len(nums)):
        # get prefix_sum from 0 to i
        prefix_sum += nums[i]
        # if there is prefix_sum is (prefix_sum - k), which will match
        if (prefix_sum - k) in sum_to_index_map:
            # get ending with i, and sum is k sub array lenth
            length = i + 1 - sum_to_index_map[prefix_sum - k]
            # update answer to min
            answer = min(answer, length)
        # store to dict
        sum_to_index_map[prefix_sum] = i + 1
        print('sum is ', prefix_sum, 'map for index ',
              i, 'is: ', sum_to_index_map)
    # if answer is +inf, no answer return -1, else return answer
    print('final map is ', sum_to_index_map)
    return -1 if (answer == float('inf')) else answer


def minSubArrayLen2(nums, target):
    # TC O(N) SC: O(1)
    l, total = 0, 0
    res = float('inf')
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(res, (r-l+1))
            total -= nums[l]
            l += 1
    return 0 if res == float('inf') else res


nums = [3, 1, -1, 5, 7]
k = 12

result = minSubArrayLen1(nums, k)
print('answer is ', result)
