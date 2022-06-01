class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # This really shouldn't be a hard problem and the acceptance rate shows, it is medium at best. 
        # Runtime: O(n)
        # Space: O(1)
        # Due to the nature of the problem, it is impossible to avoid either getting the size of the linked list or back tracking, thus the best possible solution will visit every node at least 2. I chose to count the size of the list instead of backtracking as backtracking requires a nested loop, which I thought would be gross, but I believe this solution is just as gross due to the extra pointers and values involved. There really isn't much readability optimization possible.
        curr_node = head
        size = 0
        curr_spot = 0
        while curr_node:
            curr_node = curr_node.next
            size += 1
        group_begin = head
        group_begin_prev = None
        curr_size = 1
        curr_node = head.next
        prev_node = head
        first_group = True
        while curr_node:
            if curr_size < k:
                curr_size += 1
                curr_node_next = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = curr_node_next
            else:
                if first_group:
                    head.next = curr_node
                    group_begin = curr_node
                    group_begin_prev = head
                    head = prev_node
                    first_group = False
                else:
                    group_begin_prev.next = prev_node
                    group_begin.next = curr_node
                    group_begin_prev = group_begin
                    group_begin = curr_node
                curr_size = 1 
                prev_node = curr_node
                curr_node = curr_node.next
                curr_spot += k
                if size-curr_spot < k:
                    break

            if size==k:
                head.next = None
                head = prev_node
            elif size-curr_spot == k:
                group_begin_prev.next = prev_node
                group_begin.next = None
            return head


# About 30% smaller code, but much harder to read:
    curr_node, size, curr_spot = head, 0, 0
    size = curr_spot = 0
    while curr_node:
        curr_node = curr_node.next
        size += 1
    group_begin, group_begin_prev, curr_size = head, None, 1
    curr_node, prev_node, first_group, curr_node_next = head.next, head, True, None
    while curr_node:
        if curr_size < k:
            curr_size += 1
            curr_node_next, curr_node.next = curr_node.next, prev_node
            prev_node, curr_node = curr_node, curr_node_next
        else:
            if first_group:
                head.next = group_begin = curr_node
                group_begin_prev, head, first_group = head, prev_node, False
            else:
                group_begin_prev.next, group_begin.next = prev_node, curr_node
                group_begin_prev, group_begin = group_begin, curr_node
            curr_size, prev_node, curr_node, curr_spot = 1, curr_node, curr_node.next, curr_spot + k 
            if size-curr_spot < k:
                break

    if size==k:
        head.next, head = None, prev_node
    elif size-curr_spot == k:
        group_begin_prev.next, group_begin.next = prev_node, None
    return head
