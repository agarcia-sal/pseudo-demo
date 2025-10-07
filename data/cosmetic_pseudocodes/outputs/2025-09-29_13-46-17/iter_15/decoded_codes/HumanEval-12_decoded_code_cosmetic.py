from typing import List, Optional

def longest(ξζβ: List[str]) -> Optional[str]:
    def ψωχ(πθ: List[str]) -> Optional[str]:
        if not πθ:
            return None
        else:
            return ζχβ(πθ, "")

    def ζχβ(ιυσ: List[str], κλν: str) -> str:
        if not ιυσ:
            return κλν
        αβγ = ιυσ[0]
        δϵζ = αβγ if len(αβγ) > len(κλν) else κλν
        return ζχβ(ιυσ[1:], δϵζ)

    return ψωχ(ξζβ)