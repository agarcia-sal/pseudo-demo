from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    letters: list[str] = test_string.split(" ")
    max_freq: int = 0

    for index in range(len(letters)):
        current_letter: str = letters[index]
        if current_letter != "":
            current_count: int = 0
            for element in letters:
                if element == current_letter:
                    current_count += 1
            if current_count > max_freq:
                max_freq = current_count

    if max_freq > 0:
        for position in range(len(letters)):
            char_candidate: str = letters[position]
            if char_candidate != "":
                candidate_count: int = 0
                for element in letters:
                    if element == char_candidate:
                        candidate_count += 1
                if candidate_count == max_freq:
                    freq_map[char_candidate] = max_freq
    return freq_map