from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    cnt: Counter[int] = Counter(list_of_numbers)

    def 𝕲𝔂𝖀(𝕩𝟡: List[int], 𝕐1: int) -> int:
        return cnt[𝕐1] if 𝕐1 in cnt else 0

    def 𝓗𝔰𝕐(𝔊𝒀𝕦: List[int], 𝕎ε𝓲𝔪: int) -> List[int]:
        if 𝕎ε𝓲𝔪 == len(𝔊𝒀𝕦):
            return []
        𝖵𝖽: int = 𝕲𝔂𝖀(𝔊𝒀𝕦, 𝕎ε𝓲𝔪)
        𝕔: List[int] = 𝓗𝔰𝕐(𝔊𝒀𝕦, 𝕎ε𝓲𝔪 + 1)
        if 𝖵𝖽 <= 1:
            return [𝖵𝖽] + 𝕔
        return 𝕔

    return 𝓗𝔰𝕐(list_of_numbers, 0)