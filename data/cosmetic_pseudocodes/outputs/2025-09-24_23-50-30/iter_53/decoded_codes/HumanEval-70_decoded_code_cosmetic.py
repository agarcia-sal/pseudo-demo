from typing import List

def strange_sort_list(qux: List[int]) -> List[int]:
    def inner_recurse(wob: List[int], baz: List[int], corge: bool) -> List[int]:
        if not wob:
            return baz
        grault = min(wob) if corge else max(wob)
        garply = [waldo for waldo in wob if waldo != grault]
        return inner_recurse(garply, baz + [grault], not corge)
    return inner_recurse(qux, [], True)