from typing import List

def smallest_change(input_list: List[int]) -> int:
    def helper(counter: int, accumulator: int) -> int:
        n = len(input_list)
        if counter > (n // 2) - 1:
            return accumulator
        if input_list[counter] == input_list[n - counter - 1]:
            return helper(counter + 1, accumulator)
        return helper(counter + 1, accumulator + 1)

    return helper(0, 0)