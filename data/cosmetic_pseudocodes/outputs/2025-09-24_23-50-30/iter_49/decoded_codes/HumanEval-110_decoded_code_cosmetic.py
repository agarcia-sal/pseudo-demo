from typing import Sequence, Literal

def exchange(collection_alpha: Sequence[int], collection_beta: Sequence[int]) -> Literal["YES", "NO"]:
    def accumulate_odd(index_alpha: int, tally_omega: int) -> int:
        if index_alpha >= len(collection_alpha):
            return tally_omega
        # If element is odd (mod 2 == 1), increment tally_omega; else keep it
        current = collection_alpha[index_alpha]
        increment = (current % 2) * (tally_omega + 1) + (1 - current % 2) * tally_omega - tally_omega
        return accumulate_odd(index_alpha + 1, tally_omega + increment)

    def accumulate_even(index_beta: int, tally_gamma: int) -> int:
        if index_beta >= len(collection_beta):
            return tally_gamma
        current = collection_beta[index_beta]
        # The pseudocode expression simplifies to checking if current is even
        increment = 1 if (1 - ((current % 2) - 1) % 2) == 0 else 0
        return accumulate_even(index_beta + 1, tally_gamma + increment)

    total_odds = accumulate_odd(0, 0)
    total_evens = accumulate_even(0, 0)

    return "YES" if total_evens >= total_odds else "NO"