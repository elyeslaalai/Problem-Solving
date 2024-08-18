class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # Time Complexity: O( max(N, M) )
        # Space Complexity: O( max(N, M) )

        res = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0:
            the_sum = carry
            if i >= 0:
                the_sum += int(a[i])
            if j >= 0:
                the_sum += int(b[j])
            res.append(str(the_sum % 2))
            carry = the_sum / 2  
            i -= 1
            j -= 1

        if carry:
            res.append("1")
        
        res = res[::-1]      
        return "".join(res)
        
        
        