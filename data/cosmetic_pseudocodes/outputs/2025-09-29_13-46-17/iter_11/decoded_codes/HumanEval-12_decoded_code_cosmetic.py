from typing import List, Optional

def longest(κϴMϟ: List[str]) -> Optional[str]:
    def Ŵβ(ζΛr: str, Ξה: List[str]) -> str:
        if not Ξה:
            return ζΛr
        ψ₀ = Ξה[0]
        κχₓ = Ξה[1:]
        return Ŵβ(ψ₀ if len(ζΛr) < len(ψ₀) else ζΛr, κχₓ)

    if not κϴMϟ:
        return None

    𝙕𝚇 = Ŵβ(κϴMϟ[0], κϴMϟ[1:])
    return 𝙕𝚇