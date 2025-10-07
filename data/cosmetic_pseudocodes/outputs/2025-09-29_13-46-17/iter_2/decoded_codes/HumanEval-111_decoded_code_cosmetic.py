from typing import Dict


def histogram(test_string: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    letters_array = test_string.split(" ")
    max_occurrences = 0

    def find_max(index: int) -> None:
        nonlocal max_occurrences
        if index == len(letters_array):
            return
        current_letter = letters_array[index]
        if current_letter != "":
            def count_letter(pos: int) -> int:
                if pos == len(letters_array):
                    return 0
                return (1 if letters_array[pos] == current_letter else 0) + count_letter(pos + 1)
            occurrences = count_letter(0)
            if occurrences > max_occurrences:
                max_occurrences = occurrences
        find_max(index + 1)

    find_max(0)

    if max_occurrences > 0:
        def fill_dictionary(i: int) -> None:
            if i == len(letters_array):
                return
            letter = letters_array[i]
            def letter_count(j: int) -> int:
                if j == len(letters_array):
                    return 0
                return (1 if letters_array[j] == letter else 0) + letter_count(j + 1)
            if letter_count(0) == max_occurrences:
                frequency_map[letter] = max_occurrences
            fill_dictionary(i + 1)
        fill_dictionary(0)

    return frequency_map