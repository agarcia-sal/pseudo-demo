from typing import List

def f(integer_n: int) -> List[int]:
    result_accumulator: List[int] = []
    current_index: int = 1
    while current_index <= integer_n:
        if current_index % 2 == 0:  # even check
            temp_factorial: int = 1
            count: int = 1
            while count <= current_index:
                temp_factorial *= count
                count += 1
            result_accumulator.append(temp_factorial)
        else:
            temp_sum: int = 0
            iterator_var: int = 1
            while iterator_var <= current_index:
                temp_sum += iterator_var
                iterator_var += 1
            result_accumulator.append(temp_sum)
        current_index += 1
    return result_accumulator