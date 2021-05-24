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


def delete_duplicates(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array

    arr: List[int] = [array[0]]
    for i in range(1, len(array)):
        if array[i] != array[i - 1]:
            arr.append(array[i])

    return arr


class Solution:

    # ListNode -> Array -> ListNode
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        array = listnode_to_array(head)
        array = delete_duplicates(array)
        return array_to_listnode(array)

    def deleteDuplicatesV2(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        li = ListNode(val=None)
        p = li
        while head is not None:
            if head.val != p.val:
                p.next = head
                p = p.next

            head = head.next

        p.next = head
        p = p.next
        return li.next


if __name__ == "__main__":
    print(listnode_to_array(Solution().deleteDuplicatesV2(array_to_listnode([1, 1, 2]))))
    print(listnode_to_array(Solution().deleteDuplicatesV2(array_to_listnode([1, 1, 2, 3, 3]))))
