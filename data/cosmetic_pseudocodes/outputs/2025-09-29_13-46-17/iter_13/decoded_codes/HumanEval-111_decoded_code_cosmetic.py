from typing import Dict, List


def histogram(test_string: str) -> Dict[str, int]:
    def recur_loop1(
        ƵΔψς: Dict[str, int], Ɩκρŝ: List[str], ІӫԬ: int, λΞγτ: int
    ) -> int:
        if λΞγτ == len(Ɩκρŝ):
            return ІӫԬ
        ӷʘҳ = Ɩκρŝ[λΞγτ]
        ϙŧ咴_բւΞ = (Ɩκρŝ.count(ӷʘҳ) > ІӫԬ) and (ӷʘҳ != "")
        ӫϵẏ = max(ІӫԬ, Ɩκρŝ.count(ӷʘҳ)) if ϙŧ咴_բւΞ else ІӫԬ
        return recur_loop1(ƵΔψς, Ɩκρŝ, ӫϵẏ, λΞγτ + 1)

    def recur_loop2(
        ƵΔψς: Dict[str, int], Ɩκρŝ: List[str], ІӫԬ: int, λΞγτ: int
    ) -> Dict[str, int]:
        if λΞγτ == len(Ɩκρŝ):
            return ƵΔψς
        Ҝƨҳၰ = Ɩκρŝ[λΞγτ]
        ɥϐƹ = Ɩκρŝ.count(Ҝƨҳၰ)
        if (ɥϐƹ == ІӫԬ) and (Ҝƨҳၰ != ""):
            ƵΔψς[Ҝƨҳၰ] = ІӫԬ  # update dict with word: count
        return recur_loop2(ƵΔψς, Ɩκρŝ, ІӫԬ, λΞγτ + 1)

    ʭՔƜх = test_string.split(" ")
    ϮҪԥ𝕤 = 0
    ʧξҽΦ: Dict[str, int] = {}
    ϮҪԥ𝕤 = recur_loop1(ʧξҽΦ, ʭՔƜх, ϮҪԥ𝕤, 0)
    if ϮҪԥ𝕤 > 0:
        ʧξҽΦ = recur_loop2(ʧξҽΦ, ʭՔƜх, ϮҪԥ𝕤, 0)
    return ʧξҽΦ