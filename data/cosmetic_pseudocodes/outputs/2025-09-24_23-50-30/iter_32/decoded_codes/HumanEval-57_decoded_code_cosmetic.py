from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessEqualAndGreaterEqual')

class SupportsLessEqualAndGreaterEqual:
    def __le__(self: T, other: T) -> bool: ...
    def __ge__(self: T, other: T) -> bool: ...

def monotonic(sequence: Sequence[T]) -> bool:
    index: int = 0
    forward_running: bool = True
    backward_running: bool = True
    while index < len(sequence) - 1 and (forward_running or backward_running):
        forward_running = forward_running and (sequence[index] <= sequence[index + 1])
        backward_running = backward_running and (sequence[index] >= sequence[index + 1])
        index += 1
    return forward_running or backward_running