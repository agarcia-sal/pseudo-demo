def count_distinct_characters(input_string: str) -> int:
    letters: set[str] = set()
    position: int = 0

    while position < len(input_string):
        current_char: str = input_string[position].lower()
        if current_char not in letters:
            letters.add(current_char)
        position += 1

    return len(letters)