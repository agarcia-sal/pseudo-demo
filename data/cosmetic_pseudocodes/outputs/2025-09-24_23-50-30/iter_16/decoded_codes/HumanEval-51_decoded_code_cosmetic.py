def remove_vowels(input_string: str) -> str:
    vowels_map = {"a", "e", "i", "o", "u"}
    result_sequence = []
    idx = 0

    while idx < len(input_string):
        char_val = input_string[idx].lower()
        if char_val not in vowels_map:
            result_sequence.append(input_string[idx])
        idx += 1

    return "".join(result_sequence)