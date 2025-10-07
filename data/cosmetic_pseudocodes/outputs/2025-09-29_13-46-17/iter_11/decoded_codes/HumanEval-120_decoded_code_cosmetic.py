from typing import TypeVar, List, Callable, Sequence

T = TypeVar('T')


def maximum(lst: List[T], n: int) -> List[T]:
    if n == 0:
        return []
    else:
        def identity(x: T) -> T:
            return x
        sorted_lst = sort_non_decreasing(lst)
        # The lambda (ᵫψ → (λ υλ⁴ → υλ⁴)(ᵫψ(𝛀η→ (𝛀η; 𝛀η)))) simplifies to just identity
        # and then pipe to slice_from_end
        return slice_from_end(sorted_lst, n)


def sort_non_decreasing(lst: List[T]) -> List[T]:
    if len(lst) == 0:
        return []
    else:
        def recur(sequence: List[T]) -> List[T]:
            if len(sequence) == 1:
                return sequence
            else:
                h, *rest = sequence
                sorted_rest = recur(rest)
                return merge([h], sorted_rest)
        return recur(lst)


def merge(left: List[T], right: List[T]) -> List[T]:
    def func(l: List[T], r: List[T], acc: List[T]) -> List[T]:
        if not l:
            return r + reverse_list(acc)
        elif not r:
            return l + reverse_list(acc)
        else:
            if not (head(l) > head(r)):
                return func(tail(l), r, prepend(head(l), acc))
            else:
                return func(l, tail(r), prepend(head(r), acc))
    return func(left, right, [])


def slice_from_end(lst: List[T], n: int) -> List[T]:
    def recur_slice(N: List[T], idx: int, acc: List[T]) -> List[T]:
        if idx < len(N) - n:
            return recur_slice(N, idx + 1, acc)
        elif idx >= len(N):
            return acc
        else:
            return recur_slice(N, idx + 1, append(acc, N[idx]))
    return recur_slice(lst, 0, [])


def reverse_list(lst: List[T]) -> List[T]:
    def rev_inner(inner_lst: List[T], acc: List[T]) -> List[T]:
        if not inner_lst:
            return acc
        else:
            return rev_inner(tail(inner_lst), prepend(head(inner_lst), acc))
    return rev_inner(lst, [])


def head(lst: Sequence[T]) -> T:
    return lst[0]


def tail(lst: Sequence[T]) -> List[T]:
    return lst[1:]


def prepend(hd: T, tl: List[T]) -> List[T]:
    return [hd] + tl


def append(lst: List[T], el: T) -> List[T]:
    return lst + [el]


def length(lst: List[T]) -> int:
    return len(lst)