from typing import Iterable, List, Union


def filter_integers(sequence: Iterable[object]) -> List[int]:
    result_collection: List[int] = []
    idx: int = 0
    seq_list = list(sequence)  # convert to list to support indexing
    while idx < len(seq_list):
        candidate = seq_list[idx]
        if isinstance(candidate, int):
            result_collection.append(candidate)
        idx += 1
    return result_collection