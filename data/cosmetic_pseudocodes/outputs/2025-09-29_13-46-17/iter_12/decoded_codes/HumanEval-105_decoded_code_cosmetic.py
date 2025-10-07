from typing import List, Tuple

def by_length(array_of_integers: List[int]) -> List[str]:
    def contains(collection: List[int], element: int) -> bool:
        # returns True if element is in collection, else False
        return element in collection

    dict1: List[Tuple[int, str]] = [
        (1, "One"), (2, "Two"), (3, "Three"), (4, "Four"),
        (5, "Five"), (6, "Six"), (7, "Seven"), (8, "Eight"), (9, "Nine")
    ]

    def insert_sorted(theta: int, xi: List[int]) -> List[int]:
        if not xi:
            return [theta]
        if theta >= xi[0]:
            return [theta] + xi
        return [xi[0]] + insert_sorted(theta, xi[1:])

    def foldr(
        func, acc: List[int], xs: List[int]
    ) -> List[int]:
        # foldr applies func from right to left
        for x in reversed(xs):
            acc = func(acc, x)
        return acc

    def foldr_func(acc: List[int], omega: int) -> List[int]:
        if not acc:
            return [omega]
        if omega >= acc[0]:
            return [omega] + acc
        return insert_sorted(omega, acc)

    sorted_list: List[int] = foldr(foldr_func, [], array_of_integers)

    def psi(xi: List[int], omega: List[str]) -> List[str]:
        if not xi:
            return omega
        alpha = xi[0]
        if contains([key for key, _ in dict1], alpha):
            # find value for key alpha
            val = next(v for k, v in dict1 if k == alpha)
            return psi(xi[1:], omega + [val])
        return psi(xi[1:], omega)

    return psi(sorted_list, [])