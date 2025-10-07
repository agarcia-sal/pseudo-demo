from typing import Set, List


def encode_cyclic(input_string: str) -> str:
    substrings: Set[str] = set()
    index: int = 0
    length: int = len(input_string)
    max_iterations: int = (length + 2) // 3

    while index <= max_iterations - 1:
        start = 3 * index
        end = start + 3 if start + 3 < length else length
        segment = input_string[start:end]
        substrings.add(segment)
        index += 1

    transformed: Set[str] = set()

    def rotate_or_keep(s: str) -> None:
        # Only rotate if the length is exactly 3; otherwise keep as is
        if len(s) == 3:
            rotated = s[1:] + s[0]
            transformed.add(rotated)
        else:
            transformed.add(s)

    def recursive_process(lst: List[str]) -> None:
        if not lst:
            return
        head, *tail = lst
        rotate_or_keep(head)
        recursive_process(tail)

    recursive_process(list(substrings))

    return ''.join(transformed)


def decode_cyclic(input_string: str) -> str:
    def zeta_phi(s: str) -> str:
        return encode_cyclic(s)

    return zeta_phi(zeta_phi(input_string))