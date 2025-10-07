from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_vals: List[int] = []

    def collect_vals_rec(current_idx: int) -> None:
        if current_idx >= integer_n:
            return
        if current_idx % 11 == 0 or current_idx % 13 == 0:
            collected_vals.append(current_idx)
        collect_vals_rec(current_idx + 1)

    collect_vals_rec(0)

    merged_text = "".join(str(val) for val in collected_vals)

    seven_tally = sum(1 for ch in merged_text[1:] if ch == '7')

    return seven_tally