class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x != y:
                if x < y:
                    y += (-x)
                    heapq.heappush(maxHeap, -y)
                else:
                    x += (-y)
                    heapq.heappush(maxHeap, -x)
        if len(maxHeap) == 0:
            return 0
        return -maxHeap[0]
                