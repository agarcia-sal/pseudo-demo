from typing import Dict, List, Tuple

def fib(parameter_x: int) -> int:
    stack_queue: List[Tuple[int, int]] = [(parameter_x, 0)]
    result_map: Dict[int, int] = {0: 0, 1: 1}
    while stack_queue:
        number_key, state_flag = stack_queue.pop()
        if number_key in result_map:
            continue
        if state_flag == 0:
            stack_queue.append((number_key, 1))
            stack_queue.append((number_key - 1, 0))
            stack_queue.append((number_key - 2, 0))
            continue
        result_map[number_key] = result_map[number_key - 1] + result_map[number_key - 2]
    return result_map[parameter_x]