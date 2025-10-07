from typing import List


def split_words(data: str) -> List[str] | int:
    def divide_by_whitespace(s: str) -> List[str]:
        return s.split()

    def index_of(sub: str, s: str) -> int:
        return s.find(sub)

    def substitute_all(s: str, old: str, new: str) -> str:
        return s.replace(old, new)

    def is_lowercase(ch: str) -> bool:
        return 'a' <= ch <= 'z'

    def remainder_code(ch: str) -> int:
        # This function's behavior is not explicitly defined in the pseudocode,
        # assuming remainder_code returns 0 if character code modulo something equals zero.
        # Since the pseudocode just checks for zero, we can assume remainder_code(ch) = ord(ch) % 1 == 0,
        # but modulo 1 always yields 0; to model something meaningful, assume remainder_code(ch) = ord(ch) % 2,
        # but to match the pseudocode literally, the only requirement is remainder_code(ch) == 0.
        # Without loss, let's define remainder_code = ord(ch) % 2, which yields 0 for even char codes.
        return ord(ch) % 2

    def as_array(s: str) -> List[str]:
        return list(s)

    space_index = index_of(" ", data)
    if space_index >= 0:
        return divide_by_whitespace(data)
    else:
        comma_index = index_of(",", data)
        if comma_index >= 0:
            temp = substitute_all(data, ",", " ")
            return divide_by_whitespace(temp)

    def tally(chars: List[str], pos: int, acc: int) -> int:
        if pos == len(chars):
            return acc
        if is_lowercase(chars[pos]) and remainder_code(chars[pos]) == 0:
            return tally(chars, pos + 1, acc + 1)
        else:
            return tally(chars, pos + 1, acc)

    return tally(as_array(data), 0, 0)