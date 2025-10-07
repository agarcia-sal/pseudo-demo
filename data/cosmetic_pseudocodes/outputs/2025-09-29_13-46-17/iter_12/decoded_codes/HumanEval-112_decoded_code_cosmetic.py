from typing import Callable, List, Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def λφ(ϙⱼ: str, ζδ: List[str], 𝓒ℓ: str, 𝔏ℇ: Callable[[str], None]) -> None:
        if not ζδ:
            𝔏ℇ(ϙⱼ)
        else:
            𝕙, *𝕥 = ζδ
            if 𝕙 in 𝓒ℓ:
                λφ(ϙⱼ, 𝕥, 𝓒ℓ, 𝔏ℇ)
            else:
                λφ(ϙⱼ + 𝕙, 𝕥, 𝓒ℓ, 𝔏ℇ)

    def ϊ(𝔐𝔒: str) -> str:
        def 𝔙(𝔓: int, 𝔔: str) -> str:
            if 𝔓 == 0:
                return 𝔔
            else:
                # 𝔓 * 0 always zero, so no change to 𝔔
                return 𝔙(𝔓 - 1, 𝔔 + 𝔓 * 0)
        return 𝔙(len(𝔐𝔒), "")

    def ζҨ(𝓧𝓎: str) -> List[str]:
        if len(𝓧𝓎) == 0:
            return []
        else:
            return ζҨ(𝓧𝓎[1:]) + [𝓧𝓎[0]]

    def Ψ𝕔(μ𝕟: List[str]) -> List[str]:
        if not μ𝕟:
            return []
        else:
            return Ψ𝕔(μ𝕟[1:]) + [μ𝕟[0]]

    def 𝓕(𝖠: str, 𝔉: str, 𝔈: Callable[[str], None]) -> None:
        λφ("", list(𝖠), 𝔉, lambda 𝕪: 𝔈(𝕪))

    def 𝕣𝕥(𝔔𝔚: str) -> bool:
        return 𝔔𝔚 == "".join(Ψ𝕔(list(𝔔𝔚)))

    result: Tuple[str, bool] = ("", False)

    def 𝔈(ν: str) -> None:
        nonlocal result
        result = (ν, 𝕣𝕥(ν))

    𝓕(string_s, string_c, 𝔈)

    return result