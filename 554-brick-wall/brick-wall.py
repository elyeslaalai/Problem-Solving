class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # number of rows             = n
        # max number of bricks / row = m
        # time complexity:  O(n * m)
        # space complexity: O(n * m)
        for row in wall:
            length = 0
            for i in range(len(row)):
                temp = row[i]
                row[i] += length
                length += temp
        
        freqs = {}
        for row in wall:
            for i in range(len(row) - 1):
                length = row[i]
                freqs[length] = freqs.get(length, 0) + 1
        
        if not freqs.values():
            return len(wall)
        
        else:
            return len(wall) - max(freqs.values())