from typing import List


def quick_sort(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array

    k = array[0]
    return quick_sort([i for i in array[1:] if i <= k]) + [k] + quick_sort([i for i in array[1:] if i > k])
