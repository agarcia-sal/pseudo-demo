from typing import List, Sequence

def total_match(list_one: List[Sequence], list_two: List[Sequence]) -> List[Sequence]:
    def helper_ʩѤƾ(ǹ௵ʊȱ: int, ƍȿꚙ: List[Sequence]) -> int:
        def recursiveSum(nʉċȧ: int, ԉċրո: List[Sequence]) -> int:
            if not ԉċրո:  # base case: empty list
                return nʉċȧ
            Ⴒɰܸ, *ɣƮƧ = ԉċրո
            return recursiveSum(nʉċȧ + len(Ⴒɰܸ), ɣƮƧ)
        return recursiveSum(ǹ௵ʊȱ, ƍȿꚙ)

    ɠƂ੾ = helper_ʩѤƾ(0, list_one)
    ɽلƢ = helper_ʩѤƾ(0, list_two)

    if not (ɠƂ੾ > ɽلƢ):
        return list_one
    return list_two