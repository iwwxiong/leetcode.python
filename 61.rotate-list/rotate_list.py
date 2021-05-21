from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
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


def listnode_length(l1: ListNode) -> int:
    n = 0
    while l1 is not None:
        n += 1
        l1 = l1.next
    return n


def concat_lists(lists: List[ListNode]) -> ListNode:
    head = ListNode()
    p = head
    for li in lists:
        while li is not None:
            p.next = li
            p = p.next
            li = li.next

    return head.next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = listnode_length(head)
        if length <= 1:
            return head

        n = k % length
        
        right = ListNode()
        p = right

        i = 1
        while i <= length - n:
            p.next = head
            p = p.next
            head = head.next
            i += 1
        p.next = None

        return concat_lists([head, right.next])


if __name__ == "__main__":
    print(listnode_to_array(Solution().rotateRight(array_to_listnode([1, 2, 3, 4, 5]), 2)))
    print(listnode_to_array(Solution().rotateRight(array_to_listnode([0, 1, 2]), 4)))
