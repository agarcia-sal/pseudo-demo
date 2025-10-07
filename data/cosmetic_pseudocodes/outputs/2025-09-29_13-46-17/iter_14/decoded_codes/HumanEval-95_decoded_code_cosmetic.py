from typing import Any, Dict, List, Union


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    def 𝓐_λ₀(dummy: str, 𝛬φ₁: Dict[Any, Any]) -> bool:
        if len(𝛬φ₁) == 0:
            return False

        def Ϟ_β(𝜡Ψ₈: str, 𝛈Θ₄: Any, 𝛿μ₂: int) -> str:
            if not isinstance(𝛈Θ₄, str):
                return "mixed"
            if 𝜡Ψ₈ == "start":
                if 𝛈Θ₄.isupper():
                    return "upper"
                elif 𝛈Θ₄.islower():
                    return "lower"
                else:
                    return "mixed"
            elif (𝜡Ψ₈ == "upper" and not 𝛈Θ₄.isupper()) or (𝜡Ψ₈ == "lower" and not 𝛈Θ₄.islower()):
                return "mixed"
            else:
                return 𝜡Ψ₈

        def 𝜏₁(𝜡Ψ_C: str, 𝛬φ₉: List[Any], 𝛷₀: int) -> str:
            if 𝛷₀ >= len(𝛬φ₉):
                return 𝜡Ψ_C
            𝜡Ψ_NEW = Ϟ_β(𝜡Ψ_C, 𝛬φ₉[𝛷₀], 𝛷₀ + 1)
            if 𝜡Ψ_NEW == "mixed":
                return "mixed"
            return 𝜏₁(𝜡Ψ_NEW, 𝛬φ₉, 𝛷₀ + 1)

        𝛬φ₉ = list(𝛬φ₁.keys())
        𝜡Ψ_C = "start"
        𝜡Ψ_C = 𝜏₁(𝜡Ψ_C, 𝛬φ₉, 0)
        return 𝜡Ψ_C == "upper" or 𝜡Ψ_C == "lower"

    return 𝓐_λ₀("dummy", dictionary)