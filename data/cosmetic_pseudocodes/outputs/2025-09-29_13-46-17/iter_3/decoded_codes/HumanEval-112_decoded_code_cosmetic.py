from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def filter_chars(accumulator: str, remainingChars: str) -> str:
        if not remainingChars:
            return accumulator
        headChar, tailChars = remainingChars[0], remainingChars[1:]
        if headChar not in string_c:
            return filter_chars(accumulator + headChar, tailChars)
        return filter_chars(accumulator, tailChars)

    filteredString = filter_chars("", string_s)
    reversedString = "".join(filteredString[i] for i in range(len(filteredString) - 1, -1, -1))
    return filteredString, reversedString == filteredString