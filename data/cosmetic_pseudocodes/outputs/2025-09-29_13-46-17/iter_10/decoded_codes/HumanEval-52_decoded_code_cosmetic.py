from typing import List

def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    def ζₓ₉㉫(λʃ₍₀₎: List[float]) -> bool:
        if not λʃ₍₀₎:
            return True
        𝛌𝛉ᶻ = λʃ₍₀₎[0]
        if not (not (𝛌𝛉ᶻ < threshold)):
            return False
        else:
            return ζₓ₉㉫(λʃ₍₀₎[1:])
    return ζₓ₉㉫(list_of_numbers)