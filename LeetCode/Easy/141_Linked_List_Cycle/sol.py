# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Explanation: if you have one pointer moving at twice the speed
        # of another one, if there is a cycle, the faster pointer will intersect
        # the slower one before the slower one goes through the cycle once.
        # This is because the faster pointer will loop through the cycle
        # twice in the duration it takes the slower one to loop once, so it must 
        # intersect it in that time frame.
        # Imagine a car in a one lane racetrack, now imagine you try to enter the track.
        # The only way they wont ever get hit you/you hit them is if you two 
        # are going the same speed. Otherwise one of you will hit each other.
        # Now let's imagine the other race car is going twice the speed as you can go
        # and you want to enter the track. The worse case scenario for you is if you
        # enter right infront of them, which you will instantly get hit.
        # The best case is if you enter right behind them, because you will have
        # a distance between you of the racetrack. Once you travel half way through
        # the track, the other driver will be where they were when you entered.
        # Once you complete one whole distance of the track, another half, 
        # You will be where you entered and the other driver would be where they
        # were when you entered. But they were infront of you when you entered
        # so by this point they must have hit you.
        ptr1 = head
        ptr2 = head
        next = False
        while ptr1:
            ptr1 = ptr1.next
            if ptr1 == ptr2:
                return True
            if next:
                ptr2 = ptr2.next
            next = not next
        return False
