from typing import Callable, Optional, Sequence, TypeVar, Union

T = TypeVar('T')


def is_palindrome(text: Sequence[T]) -> bool:
    return _verify_palindrome(0, length(text), text)


def _verify_palindrome(pos_A: int, length_of_input: int, string_input: Sequence[T]) -> bool:
    if not (pos_A < length_of_input / 2):
        return True
    else:
        leftChar: Optional[T] = get_char(string_input, pos_A)
        rightCharPosition: int = (length_of_input - 1) - pos_A
        rightChar: Optional[T] = get_char(string_input, rightCharPosition)
        if leftChar != rightChar:
            return False
        return _verify_palindrome(pos_A + 1, length_of_input, string_input)


def length(seq: Sequence[T]) -> int:
    count_accumulator = 0
    iterator = seq_iter(seq)
    while True:
        if not has_next(iterator):
            break
        _ = get_next(iterator)
        count_accumulator += 1
    return count_accumulator


def get_char(s: Sequence[T], idx: int) -> Optional[T]:
    a = 0
    ch: Optional[T] = None
    iter_ = seq_iter(s)
    while True:
        if not has_next(iter_):
            break
        ch = get_next(iter_)
        if a == idx:
            return ch
        a += 1
    return None


def seq_iter(sequence: Sequence[T]) -> Callable[[], tuple[bool, Optional[T]]]:
    position = 0
    length_seq = length(sequence)

    def iterator() -> tuple[bool, Optional[T]]:
        nonlocal position
        if position < length_seq:
            current = sequence[position]
            position += 1
            return True, current
        else:
            return False, None

    return iterator


def has_next(iterator: Callable[[], tuple[bool, Optional[T]]]) -> bool:
    result = iterator()
    if result[0]:
        setattr(iterator, '_saved', result[1])
        return True
    else:
        return False


def get_next(iterator: Callable[[], tuple[bool, Optional[T]]]) -> Optional[T]:
    saved = getattr(iterator, '_saved', None)
    if saved is not None:
        iterator._saved = None
        return saved
    result = iterator()
    return result[1]