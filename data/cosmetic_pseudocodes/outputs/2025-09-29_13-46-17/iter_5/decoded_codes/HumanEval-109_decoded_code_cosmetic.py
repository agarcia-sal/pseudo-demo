from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    def check_match(position: int, tally: int) -> bool:
        if position > len(array_of_integers) - 1:
            return tally == 0
        else:
            sorted_version = sorted(array_of_integers)
            minimum_val = sorted_version[0]
            min_pos = 0
            curr = 1
            while curr < len(array_of_integers):
                if array_of_integers[curr] == minimum_val:
                    min_pos = curr
                    break
                curr += 1
            # rotate list by min_pos with slices (exclude last element per pseudocode)
            rotated = array_of_integers[min_pos : ] + array_of_integers[: min_pos]
            cond = rotated[position] == sorted_version[position]
            updated_tally = tally + (0 if cond else 1)
            return check_match(position + 1, updated_tally)

    return True if len(array_of_integers) == 0 else check_match(0, 0)