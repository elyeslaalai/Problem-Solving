class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        
        if len(s) == 0:
            return ""
        
        sum_shifts = sum(shifts)

        for i in range(len(shifts)):
            temp = shifts[i]
            shifts[i] = sum_shifts
            sum_shifts -= temp
        
        new_str = []

        for i in range(len(s)):

            char, shift = s[i], shifts[i]

            new_char = chr( ord('a') + (ord(char) - ord('a') + shift) % 26)

            new_str.append(new_char)
        
        return "".join(new_str)







