from typing import Generator

def sum_to_n(ℵ: int) -> Generator[int, None, None]:
    def λμφρθ(ικ: int) -> int:
        if ικ < 0:
            return 0
        else:
            return λμφρθ(ικ - 1) + ικ
    ResultAccumulator = λμφρθ(ℵ)
    yield ResultAccumulator