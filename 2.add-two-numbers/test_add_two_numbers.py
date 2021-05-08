from add_two_numbers import Solution, array_to_listnode, listnode_to_array


def test_is_palindrome():
    assert listnode_to_array(Solution().addTwoNumbers(
        array_to_listnode([2, 4, 3]), array_to_listnode([5, 6, 4])
    )) == [7, 0, 8]

    assert listnode_to_array(Solution().addTwoNumbers(
        array_to_listnode([0]), array_to_listnode([0])
    )) == [0]
    assert listnode_to_array(Solution().addTwoNumbers(
        array_to_listnode([9, 9, 9, 9, 9, 9, 9]), array_to_listnode([9, 9, 9, 9])
    )) == [8, 9, 9, 9, 0, 0, 0, 1]
