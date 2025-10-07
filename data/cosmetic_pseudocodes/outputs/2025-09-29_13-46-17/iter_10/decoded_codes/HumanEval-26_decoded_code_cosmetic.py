from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    def 𝛀ξνεμζ𝗙(list_of_numbers: List[int], ρ𝞴: List[int]) -> List[int]:
        if not ρ𝞴:
            return []
        Ϙϼ𝕔 = ρ𝞴[0]
        ψζ𝔛𝗐 = COUNT_OCCURRENCES(list_of_numbers, Ϙϼ𝕔, 0)
        if ψζ𝔛𝗐 <= 1:
            return [Ϙϼ𝕔] + 𝛀ξνεμζ𝗙(list_of_numbers, ρ𝞴[1:])
        else:
            return 𝛀ξνεμζ𝗙(list_of_numbers, ρ𝞴[1:])

    def COUNT_OCCURRENCES(lst: List[int], target: int, idx: int) -> int:
        if idx >= len(lst):
            return 0
        accum = COUNT_OCCURRENCES(lst, target, idx + 1)
        if lst[idx] == target:
            return 1 + accum
        else:
            return accum

    return 𝛀ξνεμζ𝗙(list_of_numbers, list_of_numbers)