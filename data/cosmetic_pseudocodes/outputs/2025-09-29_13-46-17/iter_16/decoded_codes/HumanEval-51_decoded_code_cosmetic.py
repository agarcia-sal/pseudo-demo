from typing import Callable


def remove_vowels(text: str) -> str:
    def ξλϞ(pβρ: str, κξς: str, ψϕ: Callable[[str], str]) -> str:
        if pβρ == '':
            return κξς
        head = pβρ[0]
        # Check if lowercase of head is not a vowel
        if ψϕ(head) not in {'a', 'e', 'i', 'o', 'u'}:
            return ξλϞ(pβρ[1:], κξς + head, ψϕ)
        else:
            return ξλϞ(pβρ[1:], κξς, ψϕ)

    ωζχ = lambda c: c.lower()
    return ξλϞ(text, '', ωζχ)