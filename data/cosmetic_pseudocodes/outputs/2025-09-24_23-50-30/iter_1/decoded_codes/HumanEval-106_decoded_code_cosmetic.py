from typing import List


def f(integer_n: int) -> List[int]:
    result_list: List[int] = []
    index: int = 1
    while index <= integer_n:
        if index % 2 == 0:
            fact: int = 1
            mul_counter: int = 1
            while mul_counter <= index:
                fact *= mul_counter
                mul_counter += 1
            result_list.append(fact)
        else:
            sum_val: int = 0
            add_counter: int = 1
            while add_counter <= index:
                sum_val += add_counter
                add_counter += 1
            result_list.append(sum_val)
        index += 1
    return result_list