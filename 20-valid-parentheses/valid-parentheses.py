class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rules = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in rules:
                stack.append(c)
            else:
                if not stack or c != rules[stack.pop()]:
                    return False
        return not stack