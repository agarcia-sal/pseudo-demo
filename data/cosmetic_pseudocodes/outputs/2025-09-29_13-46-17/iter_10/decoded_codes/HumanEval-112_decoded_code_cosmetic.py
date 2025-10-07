from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def ζₓ₈Ƥ(sₕᵣ₇: str, ƛ_ψ₃: str) -> str:
        if not sₕᵣ₇:
            return ''
        ϕₙᵘ₁ = sₕᵣ₇[0]
        ȴₚₗ₀ = ζₓ₈Ƥ(sₕᵣ₇[1:], ƛ_ψ₃)
        if ϕₙᵘ₁ not in ƛ_ψ₃:
            return ϕₙᵘ₁ + ȴₚₗ₀
        else:
            return ȴₚₗ₀

    def ߷ԟҩ(result_string: str, idx_left: int, idx_right: int) -> bool:
        if idx_left >= idx_right:
            return True
        if result_string[idx_left] != result_string[idx_right]:
            return False
        return ߷ԟҩ(result_string, idx_left + 1, idx_right - 1)

    ʭᐯ𝖟 = ζₓ₈Ƥ(string_s, string_c)
    ϻỳₒ𝒈 = len(ʭᐯ𝖟) - 1
    𓃰ᴜɽ = ߷ԟҩ(ʭᐯ𝖟, 0, ϻỳₒ𝒈)
    return ʭᐯ𝖟, 𓃰ᴜɽ