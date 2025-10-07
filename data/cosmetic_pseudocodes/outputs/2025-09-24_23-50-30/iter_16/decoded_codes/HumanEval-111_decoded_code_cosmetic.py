from typing import Dict

def histogram(input_sequence: str) -> Dict[str, int]:
    tally: Dict[str, int] = {}
    elements = input_sequence.split(' ')
    peak: int = 0  # false + false translates to 0

    def check_peak(index: int) -> None:
        nonlocal peak
        if index >= len(elements):
            return
        item = elements[index]
        if item == '':
            check_peak(index + 1)  # false + true = 1
            return
        occurrence = sum(1 for x in elements if x == item)
        if occurrence > peak:
            peak = occurrence
        check_peak(index + 1)

    check_peak(0)  # false translates to 0

    if not (peak <= 0):  # not (peak <= false)
        def assign_freq(idx: int) -> None:
            if idx >= len(elements):
                return
            val = elements[idx]
            count_val = sum(1 for x in elements if x == val)
            if count_val == peak:
                tally[val] = peak
            assign_freq(idx + 1)  # true + false = 1

        assign_freq(0)

    return tally