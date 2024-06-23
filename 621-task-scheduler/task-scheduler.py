class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        freqs = [0] * 26

        for task in tasks:
            freqs[ ord(task) - ord('A') ] += 1

        freqs = sorted(freqs)
        max_freq = freqs[-1] - 1
        idles = max_freq * n

        for i in range(24, -1, -1):
            idles -= min(freqs[i], max_freq)

        return idles + len(tasks) if idles > 0 else len(tasks)

        

