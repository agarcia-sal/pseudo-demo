from typing import List

def all_prefixes(input_string: str) -> List[str]:
    def 𝔃ᴥ₇(𝚺: str, 𝕍: List[str], 𝕵: int, 𝟙: int) -> List[str]:
        if 𝕵 < 𝟙:
            𝕍.append(𝚺[:𝕵 + 1])
            return 𝔃ᴥ₇(𝚺, 𝕍, 𝕵 + 1, 𝟙)
        else:
            return 𝕍
    return 𝔃ᴥ₇(input_string, [], 0, len(input_string))