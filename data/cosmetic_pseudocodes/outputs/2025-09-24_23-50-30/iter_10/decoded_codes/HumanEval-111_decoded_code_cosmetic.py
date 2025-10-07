from typing import Dict

def histogram(input_sequence: str) -> Dict[str, int]:
    frequencies: Dict[str, int] = {}
    words_list = input_sequence.split(" ")

    peak_frequency = 0
    for index in range(len(words_list)):
        current_item = words_list[index]
        if current_item != "":
            tally = 0
            for checker in range(len(words_list)):
                comparison_item = words_list[checker]
                if comparison_item == current_item:
                    tally += 1
            if peak_frequency < tally:
                peak_frequency = tally

    if peak_frequency <= 0:
        return frequencies

    for candidate in words_list:
        count_candidate = 0
        for comparator in words_list:
            count_candidate += 1 if comparator == candidate else 0
        if count_candidate == peak_frequency:
            frequencies[candidate] = peak_frequency

    return frequencies