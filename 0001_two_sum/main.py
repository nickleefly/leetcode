from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            if num not in hash_table:
                hash_table[num] = [i]
            else:
                hash_table[num].append(i)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_table:
                for j in hash_table[diff]:
                    if i != j:
                        return [i, j]
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            if num not in hash_table:
                hash_table[num] = [i]
            else:
                hash_table[num].append(i)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_table:
                for j in hash_table[diff]:
                    if i != j:
                        return [i, j]

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
