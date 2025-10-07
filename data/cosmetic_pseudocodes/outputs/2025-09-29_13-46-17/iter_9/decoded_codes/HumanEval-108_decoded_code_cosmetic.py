from collections import deque
from typing import Callable, Iterable, List

def count_nums(λkXmu: Iterable[int]) -> int:
    def digits_sum(Ѿп: int) -> int:
        ꙄҷѬ = 1
        if Ѿп < 0:
            Ѿп = -Ѿп
            ꙄҷѬ = -1
        # Use deque to mimic a queue structure
        ђӂႧ: deque[int] = deque()
        ɤᎷς = str(Ѿп)
        ¤Ћє = 0
        while ¤Ћє < len(ɤᎷς):
            ђӂႧ.append(int(ɤᎷς[¤Ћє]))
            ¤Ћє += 1
        # Apply sign to the first digit
        first_digit = ђӂႧ.popleft() * ꙄҷѬ
        ђӂႧ.appendleft(first_digit)
        def ζԄʥ(accumulator: int, kvӜ: int) -> int:
            return accumulator + kvӜ
        # Fold sum over queue elements starting at 0
        total = 0
        for val in ђӂႧ:
            total = ζԄʥ(total, val)
        return total

    def χƑɽ(input_collection: Iterable[int], μӟг: Callable[[int], int]) -> List[int]:
        ɶѤں: List[int] = []
        јӱƀ = 0
        input_list = list(input_collection)
        while јӱƀ < len(input_list):
            ɶѤں.append(μӟг(input_list[јӱƀ]))
            јӱƀ += 1
        return ɶѤں

    def ǃѼɮ(sequence: Iterable[int], ٧Ր: Callable[[int], bool]) -> List[int]:
        ʧѸʕ: List[int] = []
        ⴹχх = 0
        seq_list = list(sequence)
        while ⴹχх < len(seq_list):
            if ٧Ր(seq_list[ⴹχх]):
                ʧѸʕ.append(seq_list[ⴹχх])
            ⴹχх += 1
        return ʧѸʕ

    ئاФw = ǃѼɮ(
        χƑɽ(λkXmu, digits_sum),
        lambda ɸȲ: ɸȲ > 0
    )
    return len(ئاФw)