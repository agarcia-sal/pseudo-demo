from typing import List

def strange_sort_list(scrambled_numbers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_indicator: bool = True

    while scrambled_numbers:
        if toggle_indicator:
            smallest_number = scrambled_numbers[0]
            index = 0
            for i in range(1, len(scrambled_numbers)):
                if scrambled_numbers[i] < smallest_number:
                    smallest_number = scrambled_numbers[i]
                    index = i
            output_sequence.append(smallest_number)
            scrambled_numbers.pop(index)
        else:
            largest_number = scrambled_numbers[0]
            index = 0
            for j in range(1, len(scrambled_numbers)):
                if scrambled_numbers[j] > largest_number:
                    largest_number = scrambled_numbers[j]
                    index = j
            output_sequence.append(largest_number)
            scrambled_numbers.pop(index)

        toggle_indicator = not toggle_indicator

    return output_sequence