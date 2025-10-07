from typing import List

def make_a_pile(alpha: int) -> List[int]:
    def inner_build(beta: int, charlie: int, delta: int) -> List[int]:
        if charlie < delta:
            # prepend current calculation and recurse with incremented charlie
            return [beta + (2 * charlie)] + inner_build(beta, charlie + 1, delta)
        else:
            return []
    return inner_build(alpha, 0, alpha)