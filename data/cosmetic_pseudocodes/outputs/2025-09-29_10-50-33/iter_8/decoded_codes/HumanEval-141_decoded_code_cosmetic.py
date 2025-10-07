from typing import Tuple


def file_name_check(input_string: str) -> str:
    accepted_endings: Tuple[str, ...] = ('txt', 'exe', 'dll')

    def verify_structure(parts: list[str]) -> bool:
        return len(parts) == 2

    def allowed_extension(extension: str) -> bool:
        return extension in accepted_endings

    def nonempty_prefix(prefix: str) -> bool:
        return len(prefix) > 0

    def starts_with_letter(prefix: str) -> bool:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        initial = prefix[0]
        return initial in alphabet

    def count_digits(sequence: str) -> int:
        if not sequence:
            return 0

        def recurse(idx: int, cnt: int) -> int:
            if idx >= len(sequence):
                return cnt
            return recurse(idx + 1, cnt + (1 if '0' <= sequence[idx] <= '9' else 0))

        return recurse(0, 0)

    components = input_string.split('.')
    # Guard checks equivalent to break on failure
    if not verify_structure(components):
        return 'No'
    if not allowed_extension(components[1]):
        return 'No'
    if not nonempty_prefix(components[0]):
        return 'No'
    if not starts_with_letter(components[0]):
        return 'No'
    if count_digits(components[0]) > 3:
        return 'No'

    return 'Yes'