from typing import List, TypeVar

T = TypeVar('T')
S = TypeVar('S')

def intersperse(lst: List[T], sep: S) -> List[T | S]:
    if lst:
        output: List[T | S] = []
        i = 0
        while True:
            if i < len(lst) - 1:
                output.append(lst[i])
                output.append(sep)
                i += 1
            else:
                break
        output.append(lst[-1])
        return output
    else:
        return []