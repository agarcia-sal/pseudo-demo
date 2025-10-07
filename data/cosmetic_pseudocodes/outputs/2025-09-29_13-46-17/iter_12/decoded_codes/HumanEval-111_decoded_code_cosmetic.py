from typing import Dict

def histogram(αξρ: str) -> Dict[str, int]:
    λφξ: Dict[str, int] = {}
    κψν: list[str] = αξρ.split(" ")
    ζγμ: int = 0

    def λζν() -> None:
        νσξ: int = len(κψν)
        Υ: int = 0
        while True:
            if Υ == νσξ:
                return
            if κψν[Υ] != "":
                count = κψν.count(κψν[Υ])
                nonlocal ζγμ
                if count > ζγμ:
                    ζγμ = count
            Υ += 1

    λζν()

    def ωκρ() -> Dict[str, int]:
        ωκρ: Dict[str, int] = {}
        if ζγμ > 0:
            Χ: int = 0
            while True:
                if Χ == len(κψν):
                    return ωκρ
                if κψν[Χ] != "":
                    if κψν.count(κψν[Χ]) == ζγμ:
                        ωκρ[κψν[Χ]] = ζγμ
                Χ += 1
        return {}

    ωκρ_result = ωκρ()
    λφξ.update(ωκρ_result)
    return λφξ