from typing import List


def sort_numbers(alpha_sequence: str) -> str:
    digit_values: dict[str, int] = {
        'eight': 8, 'six': 6, 'one': 1, 'four': 4,
        'five': 5, 'nine': 9, 'zero': 0, 'three': 3,
        'two': 2, 'seven': 7
    }
    tokens: List[str] = []
    beta: int = 0
    length_beta: int = len(alpha_sequence)
    while beta < length_beta:
        char_to_split: str = alpha_sequence[beta]
        if char_to_split == ' ':
            beta += 1
        else:
            start_pos: int = beta
            while beta < length_beta and alpha_sequence[beta] != ' ':
                beta += 1
            extracted: str = alpha_sequence[start_pos:beta]
            if len(extracted) > 0:
                tokens.append(extracted)
    arrangement: List[str] = []
    gamma: int = 0
    while gamma < len(tokens):
        current_word: str = tokens[gamma]
        arrangement.append(current_word)
        gamma += 1
    i: int = 0
    while i < len(arrangement) - 1:
        j: int = i + 1
        while j < len(arrangement):
            if not (digit_values[arrangement[i]] <= digit_values[arrangement[j]]):
                arrangement[i], arrangement[j] = arrangement[j], arrangement[i]
            j += 1
        i += 1
    zeta: int = 0
    final_string: str = ''
    while zeta < len(arrangement):
        final_string += arrangement[zeta]
        if zeta < len(arrangement) - 1:
            final_string += ' '
        zeta += 1
    return final_string