from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    # Recursive helper function matching the original unusual name and logic
    def jF2ƒλϿŁ(m₉₈ₖ: str, ΞΨ₁θ₃: str) -> int:
        if not (len(m₉₈ₖ) < len(ΞΨ₁θ₃) or 0 > len(m₉₈ₖ) - len(ΞΨ₁θ₃)):
            if m₉₈ₖ[:len(ΞΨ₁θ₃)] == ΞΨ₁θ₃:
                return 1 + jF2ƒλϿŁ(m₉₈ₖ[1:], ΞΨ₁θ₃)
            else:
                return jF2ƒλϿŁ(m₉₈ₖ[1:], ΞΨ₁θ₃)
        return 0
    return jF2ƒλϿŁ(original_string, target_substring)