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


def listnode_length(l1: ListNode) -> int:
    n = 0
    while l1 is not None:
        n += 1
        l1 = l1.next
    return n


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = listnode_length(head)
        if n > length:
            return head

        if n == length:
            return head.next
        
        h = ListNode(val=0, next=None)
        p = h
        i = 0
        while i < length and head is not None:
            if i == length - n:
                head = head.next
                p.next = head
            else:
                p.next = head
                p = p.next
                head = head.next
            i += 1

        return h.next


if __name__ == "__main__":
    print(listnode_to_array(Solution().removeNthFromEnd(array_to_listnode([1, 2, 3, 4, 5]), 2)))
    print(listnode_to_array(Solution().removeNthFromEnd(array_to_listnode([1]), 2)))
    print(listnode_to_array(Solution().removeNthFromEnd(array_to_listnode([1, 2]), 1)))
