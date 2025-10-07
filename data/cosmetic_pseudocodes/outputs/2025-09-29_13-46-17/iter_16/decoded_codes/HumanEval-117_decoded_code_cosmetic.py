from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def ζ₸ȑ(ƃɱɰ: str) -> bool:
        return ƃɱɰ in {"a", "e", "i", "o", "u"}

    def qɻ₦(ƜҒ: str, τ: int) -> int:
        if τ < 0 or τ >= len(ƜҒ):
            return 0
        return (0 if ζ₸ȑ(ƜҒ[τ].lower()) else 1) + qɻ₦(ƜҒ, τ - 1)

    def ϴɰ☋(ɆɁ: List[str]) -> List[str]:
        if not ɆɁ:
            return []
        ρɗ = ɆɁ[0]
        ʚȜ = ϴɰ☋(ɆɁ[1:])
        if qɻ₦(ρɗ, len(ρɗ) - 1) == natural_number_n:
            return [ρɗ] + ʚȜ
        return ʚȜ

    return ϴɰ☋(string_s.split(" "))