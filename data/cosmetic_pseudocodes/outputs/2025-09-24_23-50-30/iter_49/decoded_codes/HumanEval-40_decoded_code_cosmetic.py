from typing import Sequence

def triples_sum_to_zero(container_B: Sequence[int]) -> bool:
    length = len(container_B)

    def rec_outer(pointer_M: int) -> bool:
        if pointer_M >= length - 2:
            return False

        def rec_middle(pointer_N: int) -> bool:
            if pointer_N >= length - 1:
                return rec_outer(pointer_M + 1)

            def rec_inner(pointer_P: int) -> bool:
                if pointer_P >= length:
                    return rec_middle(pointer_N + 1)

                if container_B[pointer_M] + container_B[pointer_N] + container_B[pointer_P] == 0:
                    return True
                else:
                    return rec_inner(pointer_P + 1)

            return rec_inner(pointer_N + 1)

        return rec_middle(pointer_M + 1)

    return rec_outer(0)