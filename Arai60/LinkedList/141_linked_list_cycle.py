class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast = head.next
        slow = head

        while not (fast is None or fast.next is None):
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
