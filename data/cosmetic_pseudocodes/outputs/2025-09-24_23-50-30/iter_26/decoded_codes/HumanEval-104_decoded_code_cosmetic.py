from typing import List

def unique_digits(sequence_of_positive_numbers: List[int]) -> List[int]:
    def check_all_odd(number: int, position: int, elements: List[int]) -> bool:
        if position == len(elements):
            return True
        digit = elements[position]
        return (digit % 2 != 0) and check_all_odd(number, position + 1, elements)

    accumulator: List[int] = []
    for current_item in sequence_of_positive_numbers:
        digits_list: List[int] = []
        temp_val = current_item
        while temp_val > 0:
            digits_list.insert(0, temp_val % 10)  # prepend digit to maintain original order
            temp_val //= 10
        if check_all_odd(current_item, 0, digits_list):
            accumulator.append(current_item)

    def quick_sort(lst: List[int]) -> List[int]:
        if len(lst) <= 1:
            return lst
        pivot = lst[0]
        left_partition = quick_sort([x for x in lst[1:] if x <= pivot])
        right_partition = quick_sort([x for x in lst[1:] if x > pivot])
        return left_partition + [pivot] + right_partition

    return quick_sort(accumulator)