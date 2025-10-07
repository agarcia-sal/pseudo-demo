from typing import Protocol, TypeVar, runtime_checkable

T = TypeVar('T')


@runtime_checkable
class SupportsLessThan(Protocol):
    def __lt__(self: T, other: T) -> bool:
        ...


@runtime_checkable
class LinkedCollection(Protocol[T]):
    def at(self, index: int) -> T:
        ...

    def __len__(self) -> int:
        ...


def max_element(linked_collection: LinkedCollection[T]) -> T:
    apex_candidate = linked_collection.at(0)
    read_cursor = 0
    length = len(linked_collection)
    while read_cursor < length:
        current_entity = linked_collection.at(read_cursor)
        if apex_candidate < current_entity:
            apex_candidate = current_entity
        read_cursor += 1
    return apex_candidate