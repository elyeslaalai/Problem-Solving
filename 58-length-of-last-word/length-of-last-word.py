class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length_last_word = 0
        tail = len(s) - 1
        while tail >= 0 and s[tail] == ' ':
            tail -= 1
        while tail >= 0 and s[tail] != ' ':
            tail -= 1
            length_last_word += 1
        return length_last_word