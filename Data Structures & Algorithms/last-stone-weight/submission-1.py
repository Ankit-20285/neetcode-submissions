import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Convert to a max heap using negatives
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:

            largest = -heapq.heappop(heap)
            second_largest = -heapq.heappop(heap)

            if largest != second_largest:
                heapq.heappush(heap, -(largest - second_largest))

        if len(heap) == 0:
            return 0

        return -heap[0]