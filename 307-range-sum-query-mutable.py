from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.segment_tree = [0] * (4 * len(nums))
        self.nums = nums
        self._build_tree(0, 0, len(nums)-1)

    def _build_tree(self, idx: int, left: int, right: int):
        if left == right:
            self.segment_tree[idx] = self.nums[left]
        else:
            mid = (left + right) // 2
            self._build_tree(2*idx+1, left, mid)
            self._build_tree(2*idx+2, mid+1, right)
            self.segment_tree[idx] = (self.segment_tree[2 * idx+1]
                                      + self.segment_tree[2*idx+2])

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self._update_tree(0, 0, len(self.nums)-1, index, diff)

    def _update_tree(self, idx: int, left: int, right: int,
                     index: int, diff: int):
        if left == right:
            self.segment_tree[idx] += diff
        else:
            mid = (left + right) // 2
            if index <= mid:
                self._update_tree(2*idx+1, left, mid, index, diff)
            else:
                self._update_tree(2*idx+2, mid+1, right, index, diff)
            self.segment_tree[idx] = (self.segment_tree[2 * idx+1]
                                      + self.segment_tree[2*idx+2])

    def sumRange(self, left: int, right: int) -> int:
        return self._sum_range_helper(0, 0, len(self.nums)-1, left, right)

    def _sum_range_helper(self, idx: int, left: int, right: int,
                          qleft: int, qright: int) -> int:
        if left > qright or right < qleft:
            return 0
        elif qleft <= left and qright >= right:
            return self.segment_tree[idx]
        else:
            mid = (left + right) // 2
            return (self._sum_range_helper(2*idx+1, left, mid, qleft, qright) +
                    self._sum_range_helper(2*idx+2, mid+1, right, qleft, qright))


nums = [1, 3, 5]
numArray = NumArray(nums)
print(numArray.sumRange(0, 2))
numArray.update(1, 2)
print(numArray.sumRange(0, 2))
