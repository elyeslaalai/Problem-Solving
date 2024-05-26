class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = []  
        length_diff = abs(len(a) - len(b))
        if len(a) < len(b):
            a = '0' * length_diff + a
        else:
            b = '0' * length_diff + b
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            temp_sum = int(a[i]) + int(b[i]) + carry
            ans.append(str(temp_sum % 2))
            carry = temp_sum / 2
        if carry != 0:
            ans.append('1')
        ans = ans[::-1]
        return ''.join(ans)
        

