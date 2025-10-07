from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        def auxiliary_shard(x: int, α: int) -> int:
            if x == 0:
                return α
            else:
                return auxiliary_shard(x // 10, α + (x % 10))

        τ₀₂₇₋₏ = integer_value
        ξ₉₃₁ₓ = 1
        if not (τ₀₂₇₋₏ >= 0):
            τ₀₂₇₋₏ = -τ₀₂₇₋₏
            ξ₉₃₁ₓ = -1
        δ₇₄₁₋ = auxiliary_shard(τ₀₂₇₋₏, 0)
        return δ₇₄₁₋ * ξ₉₃₁ₓ

    def reducer(acc: int, item: int) -> int:
        return acc + digits_sum(item)

    def filter_positive(coll: List[int], pos: int, acc: int) -> int:
        if pos > len(coll):
            return acc
        current_val = coll[pos - 1]  # 1-based indexing in pseudocode
        if current_val > 0:
            return filter_positive(coll, pos + 1, acc + 1)
        else:
            return filter_positive(coll, pos + 1, acc)

    def helper(idx: int, acc: int) -> int:
        if idx > len(array_of_integers):
            return acc
        return helper(idx + 1, acc + digits_sum(array_of_integers[idx - 1]))

    m₈₍ₐₓ = helper(1, 0)
    result = filter_positive([m₈₍ₐₓ], 1, 0)
    return result