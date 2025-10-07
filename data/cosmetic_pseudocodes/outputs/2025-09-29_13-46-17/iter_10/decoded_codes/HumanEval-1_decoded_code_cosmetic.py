from typing import List, Tuple


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    # Accumulators:
    # Ωƒᾭ (Sigma) : List[str], groups of balanced parentheses as strings
    # ϴɓζ (Xi)    : List[str], current collected characters including parentheses and others
    # Ǥᵫ (Delta)   : int, current nesting level of parentheses

    Sigma: List[str] = []
    Xi: List[str] = []
    Delta: int = 0

    def sub1(
        Sigma: List[str], Xi: List[str], Delta: int, char: str
    ) -> Tuple[List[str], List[str], int]:
        # char is not a parenthesis; append to current group
        return Sigma, Xi + [char], Delta

    def sub2(
        Sigma: List[str], Xi: List[str], Delta: int, char: str
    ) -> Tuple[List[str], List[str], int]:
        # char == '(', increase nesting level and append
        return Sigma, Xi + [char], Delta + 1

    def sub3(
        Sigma: List[str], Xi: List[str], Delta: int, char: str
    ) -> Tuple[List[str], List[str], int]:
        # char == ')', decrease nesting level and append
        Delta1 = Delta - 1
        Xi1 = Xi + [char]
        balanced_closed = Delta1 == 0
        Sigma_next = Sigma + ["".join(Xi1)] if balanced_closed else Sigma
        Xi_next = [] if balanced_closed else Xi1
        return Sigma_next, Xi_next, Delta1

    def sub_dispatch(
        Sigma: List[str], Xi: List[str], Delta: int, char: str
    ) -> Tuple[List[str], List[str], int]:
        if char == "(":
            return sub2(Sigma, Xi, Delta, char)
        elif char == ")":
            return sub3(Sigma, Xi, Delta, char)
        else:
            return sub1(Sigma, Xi, Delta, char)

    def fold_left(
        chars: str, acc1: List[str], acc2: List[str], acc3: int
    ) -> Tuple[List[str], List[str], int]:
        if not chars:
            return acc1, acc2, acc3
        head, tail = chars[0], chars[1:]
        acc1_n, acc2_n, acc3_n = sub_dispatch(acc1, acc2, acc3, head)
        return fold_left(tail, acc1_n, acc2_n, acc3_n)

    Sigma, _, _ = fold_left(string_of_parentheses, Sigma, Xi, Delta)
    return Sigma