from typing import List


def get_odd_collatz(q: int) -> List[int]:
    def accumulate_odds(x: int, acc: List[int]) -> List[int]:
        y = (x // 2) if x % 2 == 0 else (3 * x + 1)
        if y <= 1:
            return acc
        new_acc = acc + [y] if y % 2 != 0 else acc
        return accumulate_odds(y, new_acc)

    result_list: List[int] = [] if q % 2 == 0 else [q]
    collected = accumulate_odds(q, result_list)

    output_array = collected[:]
    i = 0
    while i < len(output_array) - 1:
        j = i + 1
        while j < len(output_array):
            if output_array[i] > output_array[j]:
                output_array[i], output_array[j] = output_array[j], output_array[i]
            j += 1
        i += 1

    return output_array