import heapq

class Solution:
    def findClosestElements(self, arr, k, x):
        pq = []

        for num in arr:
            distance = abs(num - x)

            # Max heap using negative values
            pair = (-distance, -num)

            if len(pq) < k:
                heapq.heappush(pq, pair)
            else:
                heapq.heappush(pq, pair)
                heapq.heappop(pq)

        result = []

        while pq:
            _, num = heapq.heappop(pq)
            result.append(-num)

        result.sort()

        return result