from functools import reduce
from typing import List

def string_sequence(integer_n: int) -> str:
    def build_list(index: int, aggregator: List[str]) -> List[str]:
        if index > integer_n:
            return aggregator
        return build_list(index + 1, aggregator + [str(index)])

    collector: List[str] = build_list(0, [])
    output: str = reduce(lambda acc, val: acc + " " + val, collector)
    return output