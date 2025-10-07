from typing import List


def parse_music(music_string: str) -> List[int]:
    def func_χ𝜙Ξσσꙮτν(𝕐∪ₓΛ: List[str]) -> List[int]:
        def 𝑆(𝑎: List[int], 𝑒: int) -> List[int]:
            if 𝑒 >= len(𝕐∪ₓΛ):
                return 𝑎
            Ϫ_𝖴𝚁𝒍 = 𝕐∪ₓΛ[𝑒]
            if Ϫ_𝖴𝚁𝒍 == '':
                return 𝑆(𝑎, 𝑒 + 1)
            if Ϫ_𝖴𝚁𝒍 == 'o|':
                𝖳ƛℑ = 2
            elif Ϫ_𝖴𝚁𝒍 == 'o':
                𝖳ƛℑ = 4
            elif Ϫ_𝖴𝚁𝒍 == '.|':
                𝖳ƛℑ = 1
            else:
                𝖳ƛℑ = 0
            return 𝑆(𝑎 + [𝖳ƛℑ], 𝑒 + 1)
        return 𝑆([], 0)

    ʤϊЈᾡ𝜅ƗꝚ = music_string.split(' ')
    𝓈𝓁𝓊φ = func_χ𝜙Ξσσꙮτν(ʤϊЈᾡ𝜅ƗꝚ)
    return 𝓈𝓁𝓊φ