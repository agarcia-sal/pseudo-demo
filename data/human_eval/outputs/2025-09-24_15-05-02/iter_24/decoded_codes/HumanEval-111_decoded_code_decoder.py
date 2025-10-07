from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    # Split the input string by spaces into list_of_letters
    list_of_letters = test_string.split()
    if not list_of_letters:
        return {}

    # Count occurrences using a dictionary for efficiency
    counts = {}
    for letter in list_of_letters:
        if letter:  # ignoring empty strings if any
            counts[letter] = counts.get(letter, 0) + 1

    if not counts:
        return {}

    max_count = max(counts.values())

    # Include all letters with count equal to max_count
    result_dictionary = {letter: count for letter, count in counts.items() if count == max_count}

    return result_dictionary