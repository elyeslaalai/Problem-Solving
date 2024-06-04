class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        ans = ""
        temp = 0

        for c in s:
            if c.isdigit():
                temp = temp * 10 + int(c)
            elif c == "[":
                stack.append(temp)
                stack.append(ans)
                temp = 0
                ans = ""
            elif c == "]":
                last_str = stack.pop()
                last_num = stack.pop()
                ans = last_str + ans * last_num
            else:
                ans += c
            
        while stack:
            ans = stack.pop() + ans

        return ans
