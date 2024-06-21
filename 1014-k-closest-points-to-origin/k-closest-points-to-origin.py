import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for x, y in points:
            p = Point(x, y)
            heapq.heappush(heap, p)
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        for point in heap:
            ans.append([point.x, point.y])
        return ans

        
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = self.distance()
    
    def __lt__(self, other):
        return self.distance > other.distance
    
    def distance(self):
        return self.x ** 2 + self.y ** 2
