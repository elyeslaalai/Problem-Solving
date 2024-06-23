class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
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
        
        max_element, max_freq = -1, 0
        for element in freqs:
            if freqs[element] > max_freq:
                max_element = element
                max_freq = freqs[element]

        res = 0 
        for row in wall:
            if max_element not in row:
                res += 1
        return res