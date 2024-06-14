class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        
        if not s or not shifts:
            return ""
        
        total_shifts = []
        temp_sum = sum(shifts)

        for shift in shifts:
            total_shifts.append(temp_sum)
            temp_sum -= shift

        list_s = list(s)

        for i in range(len(s)):

            char = s[i]
            shift = total_shifts[i]
            list_s[i] = chr( ord('a') + (ord(char) - ord('a') + shift) % 26 )
        
        return "".join(list_s)



