from typing import List, Dict


def fib(integer_x: int) -> int:
    stack_list: List[int] = []
    accumulator: Dict[int, int] = {}
    stack_list.append(integer_x)

    while stack_list:
        current_val = stack_list[-1]
        if current_val == 0 or current_val == 1:
            accumulator[current_val] = current_val
            stack_list.pop()
        elif (current_val - 1) in accumulator and (current_val - 2) in accumulator:
            accumulator[current_val] = accumulator[current_val - 1] + accumulator[current_val - 2]
            stack_list.pop()
        else:
            if (current_val - 2) not in accumulator:
                stack_list.append(current_val - 2)
            if (current_val - 1) not in accumulator:
                stack_list.append(current_val - 1)

    return accumulator[integer_x]