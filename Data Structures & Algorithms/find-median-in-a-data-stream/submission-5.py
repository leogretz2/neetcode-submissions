# intended two-heap approach without max-heap
class MedianFinder:

    def __init__(self):
        # effective max heap by inserting all negatives
        self.small= []
        self.large = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)
        # transfer max across, flip
        heapq.heappush(self.large,-heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small,-heapq.heappop(self.large))
            
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2

        
        
        
        