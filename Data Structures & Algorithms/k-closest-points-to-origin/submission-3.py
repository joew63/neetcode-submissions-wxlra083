class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            heapq.heappush(maxHeap, [-distance, point])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        result = []
        for point in maxHeap:
            result.append(point[1])
        return result
        