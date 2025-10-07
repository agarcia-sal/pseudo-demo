from typing import List


def sort_array(list_of_numbers: List[int]) -> List[int]:
    def count_ones_in_binary(num: int) -> int:
        # Count number of '1's in binary representation of num
        return bin(num).count('1')

    ascending_ordered = list(list_of_numbers)
    ascending_ordered.sort()

    def sort_by_ones(arr: List[int], start: int, end: int) -> None:
        if start >= end:
            return
        pivot = arr[end]
        pivot_count = count_ones_in_binary(pivot)
        partition_index = start

        for position in range(start, end):
            if count_ones_in_binary(arr[position]) <= pivot_count:
                arr[position], arr[partition_index] = arr[partition_index], arr[position]
                partition_index += 1
        arr[partition_index], arr[end] = arr[end], arr[partition_index]
        sort_by_ones(arr, start, partition_index - 1)
        sort_by_ones(arr, partition_index + 1, end)

    sort_by_ones(ascending_ordered, 0, len(ascending_ordered) - 1)
    return ascending_ordered