from typing import List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def intersperse(pListOfNums: List[T], pDelimiter: U) -> List[T | U]:
    acc_result: List[T | U] = []
    rec_pos: int = 0
    rec_len: int = len(pListOfNums)

    def recurse() -> List[T | U]:
        nonlocal rec_pos, acc_result
        if rec_pos == rec_len:
            return acc_result
        current_elem: T = pListOfNums[rec_pos]
        is_last: bool = (rec_pos + 1) == rec_len
        if is_last:
            updated_acc = acc_result + [current_elem]
            return updated_acc
        else:
            updated_acc = acc_result + [current_elem, pDelimiter]
            rec_pos += 1
            acc_result = updated_acc
            return recurse()

    if rec_len == 0:
        return []
    else:
        return recurse()