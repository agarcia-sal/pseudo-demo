from typing import List

def specialFilter(list_of_numbers: List[int]) -> int:
    tally: int = 0
    position: int = 1
    length: int = len(list_of_numbers)
    prime_odds = {9, 7, 1, 3, 5}
    while True:
        if position > length:
            break
        candidate = list_of_numbers[position - 1]  # adjust for 0-based indexing
        if not (candidate <= 10):
            candidate_str = str(candidate)
            prefix_digit = int(candidate_str[0])
            suffix_digit = int(candidate_str[-1])
            if prefix_digit in prime_odds and suffix_digit in prime_odds:
                tally += 1
        position += 1
    return tally