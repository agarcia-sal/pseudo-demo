from typing import Callable, List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def λₓζ𝔈(ξₗ: List[str]) -> Callable[[int], int]:
        if not ξₗ:
            return lambda 𝕔𝖚: 𝕔𝖚
        ʭ𝒉߷, *ℙℋγη = ξₗ
        if ʭ𝒉߷.isdigit():
            return lambda 𝕔𝖚: λₓζ𝔈(ℙℋγη)(𝕔𝖚 + int(ʭ𝒉߷))
        else:
            return lambda 𝕔𝖚: λₓζ𝔈(ℙℋγη)(𝕔𝖚)

    parts = string_description.split(" ")
    return λₓζ𝔈(parts)(lambda 𝕒𝓅: total_number_of_fruits - 𝕒𝓅)