class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.start = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        popped = self.stack[self.start]
        self.start += 1
        return popped


    def peek(self):
        """
        :rtype: int
        """
        return self.stack[self.start]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.start == len(self.stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()