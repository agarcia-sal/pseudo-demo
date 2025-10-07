from typing import Dict


def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    letters = test_string.split(" ")

    def max_count(index: int, current_max: int) -> int:
        if index == len(letters):
            return current_max
        curr_letter = letters[index]
        count_curr = sum(1 for L in letters if L == curr_letter)
        new_max = current_max
        if curr_letter != "" and count_curr > current_max:
            new_max = count_curr
        return max_count(index + 1, new_max)

    maximum_count = max_count(0, 0)

    def fill_freq(index: int) -> None:
        if index == len(letters):
            return
        curr_letter = letters[index]
        count_curr = sum(1 for L in letters if L == curr_letter)
        if count_curr == maximum_count:
            freq_map[curr_letter] = maximum_count
        fill_freq(index + 1)

    if maximum_count > 0:
        fill_freq(0)
    return freq_map