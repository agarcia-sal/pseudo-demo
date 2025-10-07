from typing import List

def strange_sort_list(numbers_collection: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_indicator: bool = True
    numbers = numbers_collection[:]  # copy to avoid mutating input
    while numbers:
        if toggle_indicator:
            chosen_value = numbers[0]
            # find minimum value in numbers
            for index in range(1, len(numbers)):
                if numbers[index] < chosen_value:
                    chosen_value = numbers[index]
        else:
            chosen_value = numbers[0]
            # find maximum value in numbers
            for index in range(1, len(numbers)):
                if numbers[index] > chosen_value:
                    chosen_value = numbers[index]
        output_sequence.append(chosen_value)
        # remove the first occurrence of chosen_value
        for pos in range(len(numbers)):
            if numbers[pos] == chosen_value:
                del numbers[pos]
                break
        toggle_indicator = not toggle_indicator
    return output_sequence