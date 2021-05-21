from typing import List, Dict


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


def delete_duplicates_array(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array

    obj: Dict[int, int] = {}
    for i in array:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 0

    return [k for k, v in obj.items() if v == 0]


class Solution:
    # 转换成数组，去重，转换成链表
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        array = listnode_to_array(head)
        array = delete_duplicates_array(array)
        return array_to_listnode(array)

    # 双指针迭代
    # def deleteDuplicatesV2(self, head: ListNode) -> ListNode:
    #     if head is None:
    #         return head

    #     li = ListNode()
    #     p = li
    #     p.next = head
    #     cur = head
    #     while cur is not None and cur.next is not None:
    #         pass

    #     return li.next


if __name__ == "__main__":
    # print(delete_duplicates_array([1, 1, 2, 2, 3, 4, 5, 6, 6]))
    print(listnode_to_array(Solution().deleteDuplicates(array_to_listnode([1, 2, 3, 3, 4, 4, 5]))))
    print(listnode_to_array(Solution().deleteDuplicatesV2(array_to_listnode([1, 2, 3, 3, 4, 4, 5]))))
