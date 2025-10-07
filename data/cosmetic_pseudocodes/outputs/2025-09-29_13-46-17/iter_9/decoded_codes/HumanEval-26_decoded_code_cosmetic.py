from collections import Counter
from typing import Optional, Union, Sequence, TypeVar

T = TypeVar('T')

class LinkedListNode:
    def __init__(self, head: T, tail: Optional['LinkedListNode']) -> None:
        self.Head: T = head
        self.Tail: Optional['LinkedListNode'] = tail

    def __add__(self, other: Optional['LinkedListNode']) -> Optional['LinkedListNode']:
        # Assuming "+" means concatenation of linked lists
        if self is None:
            return other
        node = LinkedListNode(self.Head, self.Tail)
        if node.Tail is None:
            node.Tail = other
        else:
            node.Tail += other
        return node


def remove_duplicates(Ix6mz_yZ3: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
    ЖϠ₮ = Counter()
    current = Ix6mz_yZ3
    while current is not None:
        ЖϠ₮[current.Head] += 1
        current = current.Tail

    def ζΛ₧(φФ: T) -> bool:
        return not (ЖϠ₮[φФ] > 1)

    def ѦҨκ(ιΞ: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
        if ιΞ is None:
            return None
        ϒұWࠈ: Optional[LinkedListNode] = None
        if ζΛ₧(ιΞ.Head):
            ϒұWࠈ = LinkedListNode(ιΞ.Head, None)
        return ϒұWࠈ + ѦҨκ(ιΞ.Tail)

    return ѦҨκ(Ix6mz_yZ3)