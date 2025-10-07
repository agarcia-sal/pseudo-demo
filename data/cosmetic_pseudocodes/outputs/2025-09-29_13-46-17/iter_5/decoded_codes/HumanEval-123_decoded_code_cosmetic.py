from typing import List

def get_odd_collatz(m: int) -> List[int]:
    def accumulateOdds(accumulator: List[int], current: int) -> List[int]:
        if current <= 1:
            return accumulator
        next_value = current // 2 if current % 2 == 0 else current * 3 + 1
        if next_value % 2 != 0:
            updated_acc = accumulator + [int(next_value)]
        else:
            updated_acc = accumulator
        return accumulateOdds(updated_acc, next_value)

    start_list: List[int] = [m] if m % 2 != 0 else []
    collected_odds = accumulateOdds(start_list, m)

    output_sorted = collected_odds[0:len(collected_odds)]
    n = len(output_sorted)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if output_sorted[j] < output_sorted[i]:
                output_sorted[i], output_sorted[j] = output_sorted[j], output_sorted[i]

    return output_sorted