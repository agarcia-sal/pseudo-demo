from typing import List


def car_race_collision(fresh_param: int) -> int:
    result_list: List[int] = []
    index_counter: int = fresh_param

    def compute_power(counter: int, acc: int) -> int:
        if counter == 0:
            return acc
        return compute_power(counter - 1, acc * fresh_param)

    while index_counter > 0:
        result_list = [fresh_param] + result_list
        index_counter -= 1

    return compute_power(2, 1)