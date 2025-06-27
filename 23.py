from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            tail.next = l1 or l2
            return dummy.next

        def divideAndConquer(left: int, right: int) -> Optional[ListNode]:
            if left == right:
                return lists[left]
            mid = (left + right) // 2
            l1 = divideAndConquer(left, mid)
            l2 = divideAndConquer(mid + 1, right)
            return mergeTwoLists(l1, l2)

        return divideAndConquer(0, len(lists) - 1)