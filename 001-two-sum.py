from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        {
            3: 0,
            2: 1,
            7: 2,
            4: 3
        }

        """
        hashtable = dict()
        for i, num in enumerate(numbers):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i

        return []


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([3, 2, 7, 4], 6))
