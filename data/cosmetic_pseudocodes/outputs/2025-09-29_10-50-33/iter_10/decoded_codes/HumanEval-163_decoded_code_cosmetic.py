from typing import List

def generate_integers(integer_a: int, integer_b: int) -> List[int]:
    return helper_loop(2, 8, integer_a, integer_b, 2, [])

def helper_loop(
    fixed_min: int,
    fixed_max: int,
    param_x: int,
    param_y: int,
    step_val: int,
    acc_collection: List[int],
) -> List[int]:
    bound_low = fixed_min
    if (param_x < param_y) and (param_x < fixed_min):
        bound_low = param_x
    elif (param_y < param_x) and (param_y < fixed_min):
        bound_low = param_y

    bound_high = fixed_max
    if (param_x > param_y) and (param_x > fixed_max):
        bound_high = param_x
    elif (param_y > param_x) and (param_y > fixed_max):
        bound_high = param_y

    def recursive_collect(current: int) -> List[int]:
        if current > bound_high:
            return acc_collection
        if (current % step_val) == 0:
            return recursive_collect(current + 1) + [current]  # add current before recursive return
        else:
            return recursive_collect(current + 1)

    # Note: In the original pseudocode, the collection accumulates on unwinding recursion.
    # To maintain the order as in the pseudocode (accumulating in forward order), reverse addition order:
    # The pseudocode accumulates in acc_collection + [current], which means current is appended on the right.
    # Since recursive_collect calls itself first, we must append after the recursive call returns.
    # Adjust to:
    def recursive_collect(current: int) -> List[int]:
        if current > bound_high:
            return acc_collection
        rest = recursive_collect(current + 1)
        if (current % step_val) == 0:
            return [current] + rest  # prepend to keep order correct
        else:
            return rest

    return recursive_collect(bound_low)