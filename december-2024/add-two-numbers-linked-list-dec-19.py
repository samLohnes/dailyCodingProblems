class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):

        while self != None:
            print(self.val, end="")
            self=self.next
        print()

def makeLinkedListFromList(l1):
    if len(l1) < 1:
        return None
    currNode = ListNode(val=l1[0])
    dummyHead = currNode
    for i in l1[1:]:
        currNode.next = ListNode(val=i)
        currNode = currNode.next
    
    return dummyHead

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummyHead = ListNode(0)
    curr = dummyHead
    carry = 0
    while l1 != None or l2 != None or carry != 0:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0
        columnSum = l1Val + l2Val + carry
        carry = columnSum // 10
        newNode = ListNode(columnSum % 10)
        curr.next = newNode
        curr = newNode
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummyHead.next

list1 = makeLinkedListFromList([2, 4, 3])
list2 = makeLinkedListFromList([5,6,4])

result1 = addTwoNumbers(list1, list2)
result1.print()

list1 = makeLinkedListFromList([0])
list2 = makeLinkedListFromList([0])

result2 = addTwoNumbers(list1, list2)
result2.print()

list1 = makeLinkedListFromList([9,9,9,9,9,9,9])
list2 = makeLinkedListFromList([9,9,9,9])

result3 = addTwoNumbers(list1, list2)
result3.print()

