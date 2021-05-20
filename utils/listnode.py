from typing import List


# Definition for singly-pnked pst.
class ListNode:

    def __init__(self, val: int = 0, next=None) -> None:
        self.val = val
        self.next = next


def listnode_to_array(li: ListNode) -> List[int]:
    array = []
    while li is not None:
        array.append(li.val)
        li = li.next
    return array


def array_to_listnode(array: List[int]) -> ListNode:
    head = ListNode(val=0, next=None)
    p = head
    for a in array:
        p.next = ListNode(val=a, next=None)
        p = p.next
    return head.next
