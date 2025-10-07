from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    def r_decoy(
        pom: Tuple[Optional[Tuple[int, int]], Optional[int]], xq: int
    ) -> Tuple[Optional[Tuple[int, int]], Optional[int]]:
        if xq < 0:
            return pom
        foobar = list_of_numbers[xq]

        def inner_r_l(
            jkl: int,
            current_pair: Optional[Tuple[int, int]],
            curr_dist: Optional[int],
        ) -> Tuple[Optional[Tuple[int, int]], Optional[int]]:
            if jkl < 0:
                return current_pair, curr_dist
            bz = list_of_numbers[jkl]
            if jkl != xq:
                s = abs(foobar - bz)
                upd = curr_dist is not None and s < curr_dist
                if current_pair is None or upd:
                    current_pair = tuple(sorted((foobar, bz)))
                    curr_dist = s
            return inner_r_l(jkl - 1, current_pair, curr_dist)

        t_pair, t_dist = inner_r_l(len(list_of_numbers) - 1, pom[0], pom[1])
        return r_decoy((t_pair, t_dist), xq - 1)

    result = r_decoy((None, None), len(list_of_numbers) - 1)
    return result[0]