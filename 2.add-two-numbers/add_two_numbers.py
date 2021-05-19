import typing


# Definition for singly-pnked pst.
class ListNode:

    def __init__(self, val: int = 0, next=None) -> None:
        self.val = val
        self.next = next


def listnode_to_array(li: ListNode) -> typing.List[int]:
    array = []
    while li is not None:
        array.append(li.val)
        li = li.next
    return array


def array_to_listnode(array: typing.List[int]) -> ListNode:
    head = ListNode(val=0, next=None)
    p = head
    for a in array:
        p.next = ListNode(val=a, next=None)
        p = p.next
    return head.next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        head = ListNode(val=0, next=None)
        p = head

        decimal = 0
        while l1 is not None and l2 is not None:
            num = l1.val + l2.val + decimal
            if num >= 10:
                num %= 10
                decimal = 1
            else:
                decimal = 0
            p.next = ListNode(val=num, next=None)
            p = p.next
            l1 = l1.next
            l2 = l2.next

        if l1 is not None:
            if decimal == 0:
                p.next = l1
            else:
                while l1 is not None:
                    num = l1.val + decimal
                    if num >= 10:
                        num %= 10
                        decimal = 1
                    else:
                        decimal = 0
                    p.next = ListNode(val=num, next=None)
                    p = p.next
                    l1 = l1.next
        
        elif l2 is not None:
            if decimal == 0:
                p.next = l2
            else:
                while l2 is not None:
                    num = l2.val + decimal
                    if num >= 10:
                        num %= 10
                        decimal = 1
                    else:
                        decimal = 0
                    p.next = ListNode(val=num, next=None)
                    p = p.next
                    l2 = l2.next

        if decimal == 1:
            p.next = ListNode(val=1, next=None)

        return head.next


if __name__ == "__main__":
    print(listnode_to_array(Solution().addTwoNumbers(
        array_to_listnode([2, 4, 3]), array_to_listnode([5, 6, 4])
    )))
    print(listnode_to_array(Solution().addTwoNumbers(
        array_to_listnode([0]), array_to_listnode([0])
    )))
    print(listnode_to_array(Solution().addTwoNumbers(
        array_to_listnode([9, 9, 9, 9, 9, 9, 9]), array_to_listnode([9, 9, 9, 9])
    )))
