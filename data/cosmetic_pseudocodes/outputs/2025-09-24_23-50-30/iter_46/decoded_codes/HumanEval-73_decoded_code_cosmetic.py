from typing import List

def smallest_change(input_list: List[int]) -> int:
    def helper(counter: int, accumulator: int) -> int:
        if counter < len(input_list) / 2:
            if input_list[counter] != input_list[len(input_list) - counter - 1]:
                return helper(counter + 1, accumulator + 1)
            else:
                return helper(counter + 1, accumulator)
        return accumulator
    return helper(0, 0)