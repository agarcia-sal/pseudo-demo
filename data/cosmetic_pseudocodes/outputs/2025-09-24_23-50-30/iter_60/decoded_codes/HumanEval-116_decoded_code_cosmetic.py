from typing import List


def sort_array(epsilon: List[int]) -> List[int]:
    def helper(zeta: List[int], eta: int) -> List[int]:
        if eta == len(zeta) - 1:
            return zeta
        if zeta[eta] > zeta[eta + 1]:
            zeta[eta], zeta[eta + 1] = zeta[eta + 1], zeta[eta]
            return helper(zeta, 0)
        return helper(zeta, eta + 1)

    beta = helper(epsilon[:], 0)  # Work on a copy to avoid side effects

    def count_ones(gamma: int) -> int:
        delta = bin(gamma)[2:]  # binary string without '0b' prefix

        def count_chars(index: int, acc: int) -> int:
            if index == len(delta):
                return acc
            if delta[index] == '1':
                return count_chars(index + 1, acc + 1)
            return count_chars(index + 1, acc)

        return count_chars(0, 0)

    def sort_by_key(lst: List[int], start: int) -> List[int]:
        if start == len(lst) - 1:
            return lst
        if count_ones(lst[start]) > count_ones(lst[start + 1]):
            lst[start], lst[start + 1] = lst[start + 1], lst[start]
            return sort_by_key(lst, 0)
        return sort_by_key(lst, start + 1)

    return sort_by_key(beta, 0)