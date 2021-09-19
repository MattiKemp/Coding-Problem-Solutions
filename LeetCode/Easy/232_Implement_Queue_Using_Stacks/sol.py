class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.front = deque()
        self.end = deque()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.end.appendleft(x)
    
    # Pop and peek are amortized O(1) since the most 
    # all the elements in the queue are ever interacted with is O(2*n).
    # Which occurs when pop or peek is called when the second stack is 
    # empty: To push all the elements into the queue is O(n), so O(1) per call.
    # If we want to remove all the elements from the queue 
    # it will take n operations to move all the elements in 
    # the first stack to the second,
    # and then n operations to remove all the elements from the
    # second stack. 2*n is O(n). Since we call pop n times to remove
    # all n elements from the queue, pop is O(1) averaged over all
    # the calls to pop. Even though there will be at least one call to pop
    # that takes O(n) operations in the process.
    # is empty just checks the length of both stacks which is O(1) for each call. 
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.front)==0:
            while len(self.end) > 0:
                self.front.appendleft(self.end.popleft())
        return self.front.popleft()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.front)==0:
            while len(self.end) > 0:
                self.front.appendleft(self.end.popleft())
        top = self.front.popleft()
        self.front.appendleft(top)
        return top
        
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.front) == 0 and len(self.end)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
