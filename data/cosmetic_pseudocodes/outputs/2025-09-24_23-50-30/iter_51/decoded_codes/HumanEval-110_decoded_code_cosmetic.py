from typing import Sequence

def exchange(sequence_alpha: Sequence[int], sequence_beta: Sequence[int]) -> str:
    def scan_odd(index_om: int, odd_sum: int) -> int:
        if index_om < len(sequence_alpha):
            if sequence_alpha[index_om] % 2 == 1:
                return scan_odd(index_om + 1, odd_sum + 1)
            else:
                return scan_odd(index_om + 1, odd_sum)
        return odd_sum

    def scan_even(counter_pi: int, even_sum: int) -> int:
        if counter_pi < len(sequence_beta):
            if sequence_beta[counter_pi] % 2 == 0:
                return scan_even(counter_pi + 1, even_sum + 1)
            else:
                return scan_even(counter_pi + 1, even_sum)
        return even_sum

    total_odds = scan_odd(0, 0)
    total_evens = scan_even(0, 0)

    return "YES" if total_evens - total_odds >= 0 else "NO"