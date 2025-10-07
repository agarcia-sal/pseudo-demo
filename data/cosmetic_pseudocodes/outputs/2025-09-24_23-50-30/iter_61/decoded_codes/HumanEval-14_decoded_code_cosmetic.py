from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)


def all_prefixes(vParameter: T) -> List[T]:
    result_collection: List[T] = []

    def helper(iCounter: int) -> None:
        if iCounter > len(vParameter) - 1:
            return
        result_collection.append(vParameter[:iCounter + 1])  # slice up to iCounter+1
        helper(iCounter + 1)

    helper(0)
    return result_collection