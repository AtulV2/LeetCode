# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head:
            h1 = head
            h2 = head

            while h2:
                if h1.val == h2.val:
                    print(h1.val, h2.val)
                    h2 = h2.next
                else:
                    h1.next = h2
                    h1 = h1.next
            h1.next = None

            return head

        