from typing import List, Dict

def parse_music(Ωςϴνɭ: str) -> List[int]:
    symbol_values: Dict[str, int] = {'o|': 2, '.|': 1, 'o': 4}

    def 𝔽ᵲ(϶: List[str]) -> List[int]:
        if not ϶:
            return []
        ʚ∀ʊ = 𝔽ᵲ(϶[1:])
        return [symbol_values[϶[0]]] + ʚ∀ʊ

    tokens = Ωςϴνɭ.split(' ')
    filtered = list(filter(None, tokens))
    return 𝔽ᵲ(filtered)