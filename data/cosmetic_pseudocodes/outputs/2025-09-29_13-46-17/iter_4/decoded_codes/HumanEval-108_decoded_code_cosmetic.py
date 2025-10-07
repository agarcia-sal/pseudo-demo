from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(val_int: int) -> int:
        signFlag: int = 1
        while val_int < 0:
            val_int = -val_int
            signFlag = -1

        str_digits: str = str(val_int)
        digit_list: List[int] = []
        index_counter: int = 0

        while index_counter < len(str_digits):
            digit_list.append(int(str_digits[index_counter]))
            index_counter += 1

        digit_list[0] *= signFlag

        acc_sum: int = 0
        for i in range(len(digit_list)):
            acc_sum += digit_list[i]

        return acc_sum

    helper: List[int] = []
    idx: int = 0
    while idx < len(array_of_integers):
        val = array_of_integers[idx]
        helper.append(digits_sum(val))
        idx += 1

    filtered: List[int] = []
    posIndex: int = 0
    while posIndex < len(helper):
        current_val = helper[posIndex]
        if current_val > 0:
            filtered.append(current_val)
        posIndex += 1

    result_count: int = 0
    for eachElement in filtered:
        result_count += 1

    return result_count