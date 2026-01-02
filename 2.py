class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        headNode = ListNode(0)
        result = headNode
        
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            
            res = a + b + carry
            carry = res // 10

            newNode = ListNode(res % 10)
            result.next = newNode
            result = newNode

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return headNode.next
