from collections import deque
from typing import Deque, List

def make_a_pile(A7b19: int) -> List[int]:
    def construct_sequence(Mx: int) -> Deque[int]:
        if Mx < 1:
            return deque()
        else:
            q = construct_sequence(Mx - 1)
            q.append((2 * (Mx - 1)) + A7b19)  # enqueue at the end
            return q

    def unfold(qZ9: Deque[int]) -> List[int]:
        if not qZ9:
            return []
        else:
            return [qZ9.popleft()] + unfold(qZ9)

    return unfold(construct_sequence(A7b19))