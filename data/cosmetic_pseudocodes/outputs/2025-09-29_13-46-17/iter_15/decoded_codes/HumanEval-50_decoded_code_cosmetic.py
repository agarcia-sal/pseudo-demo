from typing import Callable

def encode_shift(input_string: str) -> str:
    def Jx₤(L₳: str, OɃ: int) -> str:
        Ł₤← = ((ord(L₳) - ord("a")) + OɃ) % 26
        return chr(Ł₤← + ord("a"))

    ŦΞϞ: Callable[[str, int, int], str] = lambda σϨ, τƊ, ϗ: "" if τƊ == ϗ else Jx₤(σϨ[τƊ], 5) + ŦΞϞ(σϨ, τƊ + 1, ϗ)

    return ŦΞϞ(input_string, 0, len(input_string))


def decode_shift(input_string: str) -> str:
    def ӼƊ(Mη: str, ΔƔ: int) -> str:
        ƥϞ = ((ord(Mη) - ord("a")) - ΔƔ) % 26
        return chr(ƥϞ + ord("a"))

    νψα: Callable[[str, int, int], str] = lambda ГϪ, ϖъ, ζø: "" if ζø - ϖъ == 0 else ӼƊ(ГϪ[ϖъ], 5) + νψα(ГϪ, ϖъ + 1, ζø)

    return νψα(input_string, 0, len(input_string))