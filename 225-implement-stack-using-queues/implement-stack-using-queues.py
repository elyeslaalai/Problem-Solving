from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue = deque()
        self.size = 0


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        self.size += 1   


    def pop(self):
        """
        :rtype: int
        """
        self.size -= 1
        return self.queue.pop()


    def top(self):
        """
        :rtype: int
        """
        popped = self.pop()
        self.push(popped)
        return popped
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()