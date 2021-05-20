import typing


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        head = ListNode(0)
        p = head
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next

            p = p.next

        if l1:
            p.next = l1
        if l2:
            p.next = l2

        return head.next


if __name__ == "__main__":
    print(listnode_to_array(Solution().mergeTwoLists(
        array_to_listnode([1, 2, 4]), array_to_listnode([1, 3, 4])
    )))
