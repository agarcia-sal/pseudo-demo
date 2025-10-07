from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def all_digits_odd_rec(x: int, y: int) -> bool:
        if y == 0:
            return True
        # Check if the last digit is odd and recurse on remaining digits
        return (y % 10) % 2 != 0 and all_digits_odd_rec(x, y // 10)

    def accumulate_odds(index: int, acc_list: List[int]) -> List[int]:
        if index == len(list_of_positive_integers):
            return acc_list
        current_number = list_of_positive_integers[index]
        condition_result = all_digits_odd_rec(current_number, current_number)
        if condition_result:
            return accumulate_odds(index + 1, acc_list + [current_number])
        else:
            return accumulate_odds(index + 1, acc_list)

    unsorted_odds = accumulate_odds(0, [])

    def insert_sorted(lst: List[int], val: int) -> List[int]:
        if not lst:
            return [val]
        elif val <= lst[0]:
            return [val] + lst
        else:
            return [lst[0]] + insert_sorted(lst[1:], val)

    def sort_list(input_list: List[int]) -> List[int]:
        if not input_list:
            return []
        return insert_sorted(sort_list(input_list[1:]), input_list[0])

    return sort_list(unsorted_odds)