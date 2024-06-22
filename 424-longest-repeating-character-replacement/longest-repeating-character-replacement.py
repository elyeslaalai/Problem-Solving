class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        

        freqs = [0] * 26
        l = r = 0
        longest_streak = 0
        highest_freq = 0

        while l <= r and r < len(s):
            new_char = s[r]
            freqs[ ord(new_char) - ord('A') ] += 1
            for i in range(len(freqs)):
                if freqs[i] > highest_freq:
                    highest_freq = freqs[i]
            length_window = r - l + 1
            if length_window - highest_freq > k:
                char_to_remove = s[l]
                freqs[ ord(char_to_remove) - ord('A') ] -= 1
                l += 1
            else:
                longest_streak = max(longest_streak, length_window)
            r += 1
        
        return longest_streak
        



            




        
        
        