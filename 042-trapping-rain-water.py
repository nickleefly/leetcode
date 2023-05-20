from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given an array of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

        Args:
            height: A list of non-negative integers.

        Returns:
            The amount of water that can be trapped after raining.
        """

        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]

        return water

if __name__ == "__main__":
    list1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    list2 = [4,2,0,3,2,5]
    print(Solution().trap(list1))
    print(Solution().trap(list2))
