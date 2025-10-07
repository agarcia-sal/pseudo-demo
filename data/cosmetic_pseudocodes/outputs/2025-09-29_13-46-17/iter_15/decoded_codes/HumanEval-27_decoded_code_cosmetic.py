from typing import Callable

def flip_case(input_string: str) -> str:
    def ⱣₓƐƟₖɣ(𝓥εℓρ: str) -> str:
        if not 𝓥εℓρ:
            return ""
        ϠɣƖ = 𝓥εℓρ[0]
        if 'A' <= ϠɣƖ <= 'Z':
            ȶƿƞ = chr(ord(ϠɣƖ) + (ord('a') - ord('A')))
        elif 'a' <= ϠɣƖ <= 'z':
            ȶƿƞ = chr(ord(ϠɣƖ) - (ord('a') - ord('A')))
        else:
            ȶƿƞ = ϠɣƖ
        return ȶƿƞ + ⱣₓƐƟₖɣ(𝓥εℓρ[1:])
    return ⱣₓƐƟₖɣ(input_string)