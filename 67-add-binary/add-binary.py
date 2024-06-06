class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        i = len(a) - 1
        j = len(b) - 1
        ans = []
        carry = 0

        while i >= 0 or j >= 0 or carry > 0:

            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0 
            the_sum = digit_a + digit_b + carry
            ans.append(str(the_sum % 2))
            carry = the_sum / 2
            i, j = i - 1, j - 1
        
        ans = ans[::-1]
        return "".join(ans)
            


