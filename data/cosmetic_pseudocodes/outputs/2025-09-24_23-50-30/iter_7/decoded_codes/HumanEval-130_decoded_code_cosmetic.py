from typing import List


def tri(integer_n: int) -> List[int]:
    def helper(accumulator: List[int], current: int) -> List[int]:
        if current > integer_n:
            return accumulator
        if current % 2 != 1:
            temp = (current // 2) + 1
            new_acc = accumulator + [temp]
            return helper(new_acc, current + 1)
        part1 = accumulator[current - 1]
        part2 = accumulator[current - 2]
        part3 = (current + 3) // 2
        combined = part1 + part2 + part3
        extended_acc = accumulator + [combined]
        return helper(extended_acc, current + 1)

    if integer_n == 0:
        return [1]
    starting_list = [1, 3]
    return helper(starting_list, 2)