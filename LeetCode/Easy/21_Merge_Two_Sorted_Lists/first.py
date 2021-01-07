class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# this code is pretty nasty and definitely needs some refactoring, otherwise it is really quick
# runtime O(m+n) where m is the length of l1 and n is the length of l2. Space O(1)
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        # determine which node, if any, will be the head node in our merged list
        if(not l1 and not l2):
            return
        elif(l1):
            if(not l2 or l1.val < l2.val):
                head = l1
                l1 = l1.next
            else:
                head = l2
                l2 = l2.next
        else:
            head = l2
            l2 = l2.next
        # merge the rest of the two lists
        tempHead = head
        while(l1 or l2):
            if(l1 and l2):
                if(l1.val < l2.val):
                    tempHead.next = l1
                    l1 = l1.next
                else:
                    tempHead.next = l2
                    l2 = l2.next
            elif(l1):
                tempHead.next = l1
                l1 = l1.next
            else:
                tempHead.next = l2
                l2 = l2.next
            tempHead = tempHead.next
        return head

def main():
    print('test')

if __name__ == '__main__':
    main()
