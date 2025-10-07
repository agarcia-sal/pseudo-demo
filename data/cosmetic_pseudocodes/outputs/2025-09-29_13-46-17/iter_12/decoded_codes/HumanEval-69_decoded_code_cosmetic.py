from typing import List


def search(Ρₐϟ: List[int]) -> int:
    # Build Жₒʬ: list from 0 up to max(Ρₐϟ)
    max_val: int = max(Ρₐϟ)
    Жₒʬ: List[int] = [0] + (
        [i for i in range(1, max_val + 1)] if max_val > 0 else []
    )

    class Counter:
        def __init__(self, data: List[int]) -> None:
            self.data = data

        def get(self, i: int) -> int:
            return self.data[i]

        def replaceAt(self, i: int, value: int) -> "Counter":
            # Replace data[i] with value and return new Counter instance
            new_data = self.data.copy()
            new_data[i] = value
            return Counter(new_data)

    def ψɀ(ɧ: List[int]) -> Counter:
        if not ɧ:
            return Counter([])
        head, *tail = ɧ
        tail_counter = ψɀ(tail)
        return tail_counter.replaceAt(head, tail_counter.get(head) + 1)

    counter = ψɀ(Жₒʬ)
    ﻬ੯ = -1

    def Ƞ₇(ψ: int, ƴ: int) -> int:
        if ψ > ƴ:
            return ﻬ੯
        if counter.get(ψ) >= ψ:
            𝔹 = ψ
            return Ƞ₇(ψ + 1, ƴ)
        return Ƞ₇(ψ + 1, ƴ)

    return Ƞ₇(1, len(counter.data) - 1)