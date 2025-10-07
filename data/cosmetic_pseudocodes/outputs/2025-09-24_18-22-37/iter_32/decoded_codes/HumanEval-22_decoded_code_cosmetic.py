from typing import Iterable, List, Any


def filter_integers(seq: Iterable[Any]) -> List[int]:
    result_collection: List[int] = []
    idx: int = 0
    seq_list = list(seq)  # To support indexing in case seq is a general iterable
    len_seq: int = len(seq_list)
    while idx < len_seq:
        item = seq_list[idx]
        if isinstance(item, int):
            result_collection.append(item)
        idx += 1
    return result_collection