from typing import Sequence, List, TypeVar

T = TypeVar('T', bound='SupportsAtAndComparison')

class SupportsAtAndComparison:
    def at(self, index: int) -> int:
        ...
    def __len__(self) -> int:
        ...

def get_positive(sequence_container: SupportsAtAndComparison) -> List[int]:
    result_collection: List[int] = []
    index_counter: int = 0
    while index_counter < len(sequence_container):
        current_value: int = sequence_container.at(index_counter)
        if current_value > 0:
            result_collection.append(current_value)
        index_counter += 1
    return result_collection