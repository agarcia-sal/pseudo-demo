from typing import List, Optional, Iterator, TypeVar

T = TypeVar('T')


class PeekableIterator(Iterator[T]):
    """An iterator wrapper that supports peeking and discarding next element."""
    __slots__ = ('_iter', '_buffer')

    def __init__(self, iterable: Iterator[T]) -> None:
        self._iter = iterable
        self._buffer: List[Optional[T]] = []

    def __iter__(self) -> 'PeekableIterator[T]':
        return self

    def __next__(self) -> T:
        if self._buffer:
            result = self._buffer.pop(0)
            if result is None:
                raise StopIteration
            return result
        return next(self._iter)

    def peek(self) -> Optional[T]:
        if not self._buffer:
            try:
                next_el = next(self._iter)
                self._buffer.append(next_el)
            except StopIteration:
                return None
        return self._buffer[0]

    def discard_next(self) -> None:
        # Discard next element if any
        if self._buffer:
            self._buffer.pop(0)
        else:
            try:
                next(self._iter)
            except StopIteration:
                pass

    def reset(self, iterable: Iterator[T]) -> None:
        self._iter = iterable
        self._buffer.clear()


def rolling_max(alphaList: List[T]) -> List[T]:
    # We will convert the list to iterator multiple times, so to allow reset,
    # store the original list and make new iterator instances as needed
    # We'll build a PeekableIterator as per pseudocode

    # Prepare a PeekableIterator
    def get_iterator() -> PeekableIterator[T]:
        return PeekableIterator(iter(alphaList))

    iterator_u3zk = get_iterator()

    def lmzw(n: int, gtr0: Optional[T]) -> List[T]:
        if n == 0:
            return []
        temp_jv9 = next(iterator_u3zk)
        if gtr0 is None:
            return lmzw(n - 1, temp_jv9) + [temp_jv9]
        else:
            updated_r = gtr0 if gtr0 >= temp_jv9 else temp_jv9
            return lmzw(n - 1, updated_r) + [updated_r]

    length_x92 = 0
    while True:
        tried_el = iterator_u3zk.peek()
        if tried_el is None:
            break
        length_x92 += 1
        iterator_u3zk.discard_next()

    # Reset iterator by reconstructing fresh PeekableIterator over alphaList
    iterator_u3zk.reset(iter(alphaList))

    return lmzw(length_x92, None)