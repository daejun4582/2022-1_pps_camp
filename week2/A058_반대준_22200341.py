def reverseList(self, head):
    prev = None
    while head.next:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    head.next = prev
    return head