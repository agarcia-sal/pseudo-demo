from typing import Set

def all_prefixes(input_string: str) -> Set[str]:
    def loop(i: int, prefixes: Set[str]) -> Set[str]:
        if i >= len(input_string):
            return prefixes
        next_set = prefixes | {input_string[:i+1]}
        return loop(i + 1, next_set)
    return loop(0, set())