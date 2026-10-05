# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            num = total % 10
            carry = total // 10

            dummy.next = ListNode(num)
            dummy = dummy.next

        return res.next
        


# time complexity: O(max(m, n)) where m and n are the lengths of the two linked lists. We traverse both linked lists once, so the time complexity is linear with respect to the length of the longer list.
# space complexity: O(max(m, n)) for the new linked list that we create to store the result. In the worst case, the sum of the two numbers can have one more digit than the longer of the two input numbers (e.g., 999 + 1 = 1000), so we may need to create a new node for each digit in the result.