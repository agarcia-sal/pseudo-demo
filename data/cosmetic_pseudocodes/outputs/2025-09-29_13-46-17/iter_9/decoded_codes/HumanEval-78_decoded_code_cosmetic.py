from typing import Sequence

def hex_key(𝛶ΛψσϾ: Sequence[str]) -> int:
    ↹⇡ζ⇨ξφ = ['B', '2', 'D', '7', '3', '5']
    ξζᏕφλ = 0
    λςχβ = 0
    Σχϊ = λςχβ < (len(𝛶ΛψσϾ) - 1)
    while Σχϊ:
        # ¬ ((𝛶ΛψσϾ[λςχβ] ∉ ↹⇡ζ⇨ξφ)) == False means 𝛶ΛψσϾ[λςχβ] ∈ ↹⇡ζ⇨ξφ
        if 𝛶ΛψσϾ[λςχβ] in ↹⇡ζ⇨ξφ:
            ξζᏕφλ += 1
        λςχβ += 1
        Σχϊ = λςχβ < (len(𝛶ΛψσϾ) - 1)
    return ξζᏕφλ