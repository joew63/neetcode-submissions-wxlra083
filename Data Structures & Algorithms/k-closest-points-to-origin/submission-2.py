class Solution:
    def kClosest(self, points, k):
        maxHeap = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2  # no need for sqrt
            heapq.heappush(maxHeap, (-dist, point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [point for (dist, point) in maxHeap]