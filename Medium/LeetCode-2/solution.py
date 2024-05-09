def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1:
        return l2
    if not l2: 
        return l1

    carry = 0
    
    sumList = ListNode()
    l3 = sumList

    while (l1 is not None and l2 is not None):
        currSum = l1.val + l2.val + carry
        carry = int(currSum/10)
        sumVal = (currSum % 10)

        sumList.next = ListNode(sumVal)
        sumList = sumList.next

        l1 = l1.next
        l2 = l2.next
    
    while (l1 is not None):
        currSum = l1.val + carry
        carry = int(currSum/10)
        sumVal = (currSum % 10)

        sumList.next = ListNode(sumVal)
        sumList = sumList.next

        l1 = l1.next

    while (l2 is not None):
        currSum = l2.val + carry
        carry = int(currSum/10)
        sumVal = (currSum % 10)

        sumList.next = ListNode(sumVal)
        sumList = sumList.next

        l2 = l2.next
    
    if carry == 1:
        sumList.next = ListNode(carry)
    
    return l3.next