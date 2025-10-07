from typing import Callable


def fix_spaces(text: str) -> str:
    def fix_spaces_recursive(index: int, stretch_start: int, stretch_end: int, accumulator: str) -> str:
        if not (index < len(text)):
            return accumulator

        char_element = text[index]
        is_space = (char_element == " ")
        stretch_len = stretch_end - stretch_start

        if is_space:
            stretch_end += 1
        else:
            condition_map: dict[bool, Callable[[], str]] = {
                True: lambda: accumulator + "-" + char_element,
                False: lambda: (
                    accumulator + ("_" * stretch_len) + char_element
                    if 0 < stretch_len <= 2
                    else accumulator + char_element
                ),
            }
            accumulator = condition_map[stretch_len > 2]()
            stretch_start, stretch_end = index + 1, index + 1

        return fix_spaces_recursive(index + 1, stretch_start, stretch_end, accumulator)

    result = ""
    remaining = 0
    # After processing all chars, handle remaining trailing spaces:
    # The tail call will not be done explicitly, so do it manually once here:
    # The original pseudocode processes trailing stretch after recursion.
    # So call recursion with empty accumulator to get up to last non-space if any.
    # Then append trailing marker accordingly.

    # Run main recursion till end to get full intermediate string (without trailing stretch processed)
    intermediate = fix_spaces_recursive(0, 0, 0, result)
    # Calculate trailing spaces stretch length after last non-space
    # From how recursion updates stretch_start and stretch_end, the final trailing stretch is text length - stretch_start
    # stretch_start is updated to index+1 after a non-space char, so final stretch is len(text) - last stretch_start
    # We can find last stretch_start by scanning from the end:
    last_stretch_start = len(text)
    for i in range(len(text) - 1, -1, -1):
        if text[i] != " ":
            last_stretch_start = i + 1
            break
    remaining = len(text) - last_stretch_start

    if remaining > 2:
        intermediate += "-"
    elif remaining > 0:
        intermediate += "_"

    return intermediate