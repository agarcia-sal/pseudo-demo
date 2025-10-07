from typing import List, Callable


def parse_music(music_string: str) -> List[int]:
    def 𝜈₉κ₁(ψ: List[str]) -> List[int]:
        ɸΔ₀Ƅ: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}

        def Ț(λ: List[str], Σ: List[int], Ƿ: Callable[[str], bool]) -> List[int]:
            if not λ:
                return Σ
            head, *tail = λ
            if Ƿ(head):
                return Ț(tail, Σ + [ɸΔ₀Ƅ[head]], Ƿ)
            else:
                return Ț(tail, Σ, Ƿ)

        return Ț(ψ, [], lambda x: x != '')

    return 𝜈₉κ₁(music_string.split(' '))