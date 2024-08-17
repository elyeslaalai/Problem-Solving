class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        couples = {
            '[': ']',
            '(': ')',
            '{': '}'
        }

        stack = []

        for c in s:

            if c in couples:
                stack.append(c)
            
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if couples[popped] != c:
                        return False

        return not stack  


