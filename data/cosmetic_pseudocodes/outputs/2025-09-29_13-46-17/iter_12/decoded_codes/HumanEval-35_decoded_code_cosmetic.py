from typing import List, Callable, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    def ζ㉿(Ψϟ: List[T]) -> T:
        max_val: T = Ψϟ[0]

        def Ϡψλ(xs: List[T]) -> T:
            if not xs:
                return max_val
            head, *tail = xs
            nonlocal max_val
            if head > max_val:
                max_val = head
            return Ϡψλ(tail)

        return Ϡψλ(Ψϟ)

    return ζ㉿(list_of_elements)