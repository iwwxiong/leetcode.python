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

    # 递归
    # FIXME Leetcode Time Limit Exceeded
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        return self.mergeTwoLists(lists[0], self.mergeKLists(lists[1:]))

    # 两两合并
    # FIXME Leetcode Time Limit Exceeded
    def mergeKListsV2(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        li = self.mergeTwoLists(lists[0], lists[1])
        for i in range(2, len(lists)):
            li = self.mergeTwoLists(li, lists[i])

        return li

    def mergeKListsV3(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        if len(lists) % 2 == 0:
            return self.mergeKListsV3([self.mergeTwoLists(lists[i], lists[i + 1]) for i in range(0, len(lists), 2)])
        else:
            return self.mergeKListsV3(
                [self.mergeTwoLists(lists[i], lists[i + 1]) for i in range(0, len(lists) - 1, 2)] + [lists[-1]]
            )


if __name__ == "__main__":
    print(listnode_to_array(Solution().mergeKListsV3(
        [array_to_listnode([1, 4, 5]), array_to_listnode([1, 3, 4]), array_to_listnode([2, 6])]
    )))
