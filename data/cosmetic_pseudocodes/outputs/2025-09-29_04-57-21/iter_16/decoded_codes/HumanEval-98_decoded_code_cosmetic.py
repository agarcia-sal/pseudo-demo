def count_upper(string_input: str) -> int:
    vowel_tally: int = 0
    position: int = 0
    while position < len(string_input):
        if string_input[position] in "AEIOU":
            vowel_tally += 1
        position += 2
    return vowel_tally