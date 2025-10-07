from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def helper(index: int, acc: List[int]) -> List[int]:
        if index > len(list_of_positive_integers):
            return sorted(acc)
        current_num = list_of_positive_integers[index - 1]

        def all_odd(digits_list: List[int]) -> bool:
            if not digits_list:
                return True
            if digits_list[0] % 2 == 0:
                return False
            return all_odd(digits_list[1:])

        digits_list = [int(d) for d in str(current_num)]
        new_acc = acc + [current_num] if all_odd(digits_list) else acc
        return helper(index + 1, new_acc)

    return helper(1, [])