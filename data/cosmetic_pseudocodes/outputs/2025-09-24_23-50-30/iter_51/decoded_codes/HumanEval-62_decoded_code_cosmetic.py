from typing import List

def derivative(sequence: List[int]) -> List[int]:
    def helper(pos: int, coll: List[int], acc: List[int]) -> List[int]:
        if pos >= len(coll):
            return acc
        else:
            return helper(pos + 1, coll, acc + [coll[pos] * pos])
    return helper(1, sequence, [])