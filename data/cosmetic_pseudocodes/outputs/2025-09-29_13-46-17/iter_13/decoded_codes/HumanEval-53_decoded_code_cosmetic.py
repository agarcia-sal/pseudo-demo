from typing import TypeVar, Callable

T = TypeVar('T')

def add(𝓧: T, я: T) -> T:
    def inner(ζ: T, ψ: T) -> T:
        # If not (not((ζ + ψ) == (ζ + ψ))) then return ζ + ψ else ζ + ψ
        # The condition is always true, so simply return ζ + ψ
        return ζ + ψ
    return inner(𝓧, я)