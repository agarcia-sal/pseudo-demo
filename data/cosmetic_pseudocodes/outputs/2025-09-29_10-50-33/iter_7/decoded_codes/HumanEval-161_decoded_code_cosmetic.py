from typing import List


def solve(text_entry: str) -> str:
    inversion_marker: bool = False
    cursor: int = 0
    char_sequence: List[str] = list(text_entry)

    def toggleCase(c: str) -> str:
        # Swap case only for ascii letters, preserve other chars (though not used for others here)
        if 'a' <= c <= 'z':
            return c.upper()
        if 'A' <= c <= 'Z':
            return c.lower()
        return c

    def reverseString(s: str) -> str:
        return s[::-1]

    def iterate_chars(pos: int) -> None:
        nonlocal inversion_marker
        if pos >= len(text_entry):
            return
        current_char: str = text_entry[pos]
        if ('A' <= current_char <= 'Z') or ('a' <= current_char <= 'z'):
            converted_char: str = toggleCase(current_char)
            char_sequence[pos] = converted_char
            inversion_marker = True
        iterate_chars(pos + 1)

    iterate_chars(cursor)
    assembled_text: str = "".join(char_sequence)
    if not inversion_marker:
        return reverseString(assembled_text)
    return assembled_text