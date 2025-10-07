from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def gather_digits(seq: List[str], accum: List[int], idx: int) -> List[int]:
        if idx >= len(seq):
            return accum
        if seq[idx].isdigit():
            return gather_digits(seq, accum + [int(seq[idx])], idx + 1)
        else:
            return gather_digits(seq, accum, idx + 1)

    tokens_list = string_description.split(" ")
    collected_numbers = gather_digits(tokens_list, [], 0)
    total_collected = sum(collected_numbers)
    return total_number_of_fruits - total_collected