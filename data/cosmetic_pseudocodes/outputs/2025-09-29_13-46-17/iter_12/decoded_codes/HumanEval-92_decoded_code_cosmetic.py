from typing import Callable, Iterable


def any_int(Ꮰ: Iterable[int], 𝒀: Iterable[int], ꙰: Iterable[int]) -> bool:
    def ╳₣(𝑨: int, 𝑩: int, 𝑫: int) -> bool:
        if not all(isinstance(x, int) for x in (𝑨, 𝑩, 𝑫)):
            return False
        return (𝑨 + 𝑩 == 𝑫) or (𝑨 + 𝑫 == 𝑩) or (𝑩 + 𝑫 == 𝑨)

    return any(
        ╳₣(a, b, c)
        for a in Ꮰ
        for b in 𝒀
        for c in ꙰
    )