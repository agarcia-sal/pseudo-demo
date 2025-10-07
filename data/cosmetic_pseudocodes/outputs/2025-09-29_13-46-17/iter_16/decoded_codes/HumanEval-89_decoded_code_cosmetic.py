from typing import Callable

def encrypt(input_string: str) -> str:
    def ϟΨξΣ(ΩΛ: str) -> str:
        if not ΩΛ:
            return ""
        ᛦɰ = ΩΛ[0]
        θσ = "abcdefghijklmnopqrstuvwxyz"
        def shift_char(џɆ: str) -> str:
            if џɆ not in θσ:
                return џɆ
            Ψμ = ((θσ.index(џɆ) + 2) * 2) % 26
            return θσ[Ψμ]
        γπ = shift_char(ᛦɰ)
        return γπ + ϟΨξΣ(ΩΛ[1:])
    return ϟΨξΣ(input_string)