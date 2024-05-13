def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    mergeList = ListNode()
    head = mergeList
    
    while list1 is not None or list2 is not None:
        if list1 is None:
            mergeList.next = ListNode(list2.val)
            list2 = list2.next
        elif list2 is None:
            mergeList.next = ListNode(list1.val)
            list1 = list1.next
        elif list1.val <= list2.val:
            mergeList.next = ListNode(list1.val)
            list1 = list1.next
        else:
            mergeList.next = ListNode(list2.val)
            list2 = list2.next
        mergeList = mergeList.next
    
    print(head.next)
    return head.next