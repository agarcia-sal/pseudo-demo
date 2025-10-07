from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    def Ξ(𝛁: int, ᒼ: List[int], ε: int) -> List[int]:
        # Stop condition: index out of bounds or last element (with epsilon logic)
        if not ((𝛁 == 0 and ε != 1) or (𝛁 < 0)):
            ᴥ = ᒼ + [list_of_numbers[ε]]
            return ᴥ
        else:
            𝚽 = ᒼ + [list_of_numbers[ε], delimiter]
            return Ξ(𝛁 - 1, 𝚽, ε + 1)

    𝛛 = len(list_of_numbers) - 1
    if 𝛛 < 0:
        return []
    return Ξ(𝛛, [], 0)