from typing import Dict

def histogram(input_sequence: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    symbols = input_sequence.split(" ")
    highest_frequency = 0

    def check_frequency(index: int) -> None:
        nonlocal highest_frequency
        if index == len(symbols):
            return
        current_entry = symbols[index]
        occurrence_count = symbols.count(current_entry)
        if occurrence_count > highest_frequency and current_entry != "":
            highest_frequency = occurrence_count
        check_frequency(index + 1)

    check_frequency(0)

    def build_frequency(index: int) -> None:
        if index == len(symbols):
            return
        current_entry = symbols[index]
        occurrence_count = symbols.count(current_entry)
        if occurrence_count == highest_frequency:
            frequency_map[current_entry] = highest_frequency
        build_frequency(index + 1)

    if highest_frequency > 0:
        build_frequency(0)

    return frequency_map