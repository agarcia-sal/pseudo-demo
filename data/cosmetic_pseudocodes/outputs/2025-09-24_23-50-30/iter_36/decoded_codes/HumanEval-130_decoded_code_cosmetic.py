from typing import List


def tri(positional_x: int) -> List[int]:
    if positional_x != 0:
        accum_list: List[int] = [1, 3]

        def loop_recursive(current_y: int, collection: List[int]) -> List[int]:
            if current_y > positional_x:
                return collection
            if current_y % 2 == 0:
                new_val = (current_y // 2) + 1
            else:
                val_a = collection[current_y - 1]
                val_b = collection[current_y - 2]
                new_val = val_a + val_b + ((current_y + 3) // 2)
            return loop_recursive(current_y + 1, collection + [new_val])

        return loop_recursive(2, accum_list)
    else:
        return [1]