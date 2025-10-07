def remove_vowels(phrase: str) -> str:
    output_string: str = ""
    cursor: int = 0
    while cursor < len(phrase):
        character: str = phrase[cursor]
        lowered_char: str = character.lower()
        if lowered_char not in {"a", "e", "i", "o", "u"}:
            output_string += character
        cursor += 1
    return output_string