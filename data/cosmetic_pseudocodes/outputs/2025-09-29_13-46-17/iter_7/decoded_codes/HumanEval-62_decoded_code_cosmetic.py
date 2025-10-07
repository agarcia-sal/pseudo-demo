from typing import List, Sequence, Tuple, TypeVar

T = TypeVar('T')

def derivative(x1GqYvWV5: Sequence[float]) -> List[float]:
    def multiplierAcc(acc: List[float], pair: Tuple[int, float]) -> List[float]:
        iHa2vW, kGrtc = pair
        if iHa2vW == 0:
            return acc
        else:
            return acc + [kGrtc * iHa2vW]
    return fold_left(multiplierAcc, [], list(enumerate(x1GqYvWV5)))

def fold_left(func, initial: T, seq: Sequence) -> T:
    acc = initial
    for item in seq:
        acc = func(acc, item)
    return acc