from typing import List, Dict, TypeVar

T = TypeVar('T', bound=object)

def common(listA: List[T], listB: List[T]) -> List[T]:
    store: Dict[T, bool] = {item: True for item in listA}
    collect: List[T] = []
    for item in listB:
        if store.get(item, False):
            collect.append(item)
            store[item] = False
    return sorted(collect)