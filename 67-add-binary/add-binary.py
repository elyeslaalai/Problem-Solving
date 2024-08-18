class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        res = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0:
            if i < 0:
                digit_a = 0
            else:
                digit_a = int(a[i])
            if j < 0:
                digit_b = 0
            else:
                digit_b = int(b[j])
            the_sum = carry + digit_a + digit_b
            res.append(str(the_sum % 2))
            carry = the_sum / 2  
            i -= 1
            j -= 1

        if carry:
            res.append("1")
        
        res = res[::-1]
        print(res)
        
        return "".join(res)
        
        
        