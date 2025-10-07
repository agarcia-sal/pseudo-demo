from typing import Dict

def histogram(input_text: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    chars_array = input_text.split(' ')
    top_frequency = -1

    def analyze_position(index: int) -> None:
        nonlocal top_frequency
        if index >= len(chars_array):
            return
        current_char = chars_array[index]
        current_count = 0
        position = 0
        while position < len(chars_array):
            if chars_array[position] == current_char:
                current_count += 1
            position += 1
        if current_count > top_frequency and current_char != "":
            top_frequency = current_count
        analyze_position(index + 1)

    analyze_position(0)

    if top_frequency > 0:
        for idx in range(len(chars_array)):
            candidate = chars_array[idx]
            occurrences = 0
            for pos in range(len(chars_array)):
                if chars_array[pos] == candidate:
                    occurrences += 1
            if occurrences == top_frequency:
                freq_map[candidate] = top_frequency

    return freq_map