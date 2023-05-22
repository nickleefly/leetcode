from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(matrix[0][j], 0, j) for j in range(n)]
        heapq.heapify(heap)
        print(heap)

        for _ in range(k - 1):
            num, i, j = heapq.heappop(heap)
            print(f'{i} {j}')
            if i < n - 1:
                print(f'{matrix[i+1][j]} {i+1} {j}')
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
                print(heap)

        return heapq.heappop(heap)[0]


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 7
print(Solution().kthSmallest(matrix, k))
