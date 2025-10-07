from typing import Iterable, Optional, Sequence, TypeVar

T = TypeVar("T", bound=Sequence[str])

def longest(container_of_texts: Iterable[Sequence[str]]) -> Optional[Sequence[str]]:
    container_list = list(container_of_texts)
    if not container_list:
        return None

    limit_length: int = max(len(text) for text in container_list)

    def find_match(seq: Sequence[Sequence[str]]) -> Optional[Sequence[str]]:
        if not seq:
            return None
        head, *tail = seq
        return head if len(head) == limit_length else find_match(tail)

    return find_match(container_list)