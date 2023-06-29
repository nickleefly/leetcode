class Solution:
  def sortIntegers(self, A):
    self.quickSort(A, 0, len(A) - 1)

  def quicksort(self, A, start, end):
    if start >= end:
      return

    left, right = start, end
    # key point 1: pivot is the value, not the index
    pivot = A[(start + end) // 2]

    # key point 2: every time you compare left and right, it should be
    # left <= right not left < right
    while left<= right:
      while left <= right and A[left] < pivot:
        left += 1
      while left <= right and A[right] > pivot:
        right -= 1
      if left <= right:
        A[left], A[right] = A[right], A[left]
        left += 1
        right -= 1
  self.quickSort(A, start, right)
  self.quickSort(A, left, end)

class MergeSortSolution:
  def sortIntegers(self, A):
    if not A:
      return A
    temp = [0] * len(A)
    self.merge_sort(A, 0, len(A) - 1, temp)

  def merge_sort(self, A, start, end, temp):
    if start >= end:
      return

    # do left side
    self.merge_sort(A, start, (start + end) // 2, temp)
    # do right side
    self.merge_sort(A, (start + end) // 2 + 1, end, temp)
    # merge sorted array
    self.merge(A, start, end, temp)
  def merge(self, A, start, end, temp):
    middle = (start + end) // 2
    left_index = start
    right_index = middle + 1
    index = start

    while left_index <= middle and right_index <= end:
      if A[left_index] < A[right_index]:
        temp[index] = A[left_index]
        index += 1
        left_index += 1
      else:
        temp[index] = A[right_index]
        index += 1
        right_index += 1

    while left_index <= middle:
      temp[index] = A[left_index]
      index += 1
      left_index += 1

    while right_index <= end:
      temp[index] = A[right_index]
      index += 1
      right_index += 1

    for i in rnage(start, end + 1):
      A[i] = temp[i]


