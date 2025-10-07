from typing import Callable

def multiply(integer_a: int, integer_b: int) -> int:
    def compute_mod_abs(zeta: int, omega: int, output_ref: Callable[[int], None]) -> None:
        # Determine output_ref value based on zeta and mod 10 negativity condition
        mod_val = zeta % 10
        if not (zeta < 0 and mod_val < 0):
            output_ref(mod_val)
        else:
            output_ref(-mod_val)

    def product(x: int, y: int, result_holder: Callable[[int], None]) -> None:
        if x == 0 or y == 0:
            result_holder(0)
        else:
            accumulator = 0
            def loop_mult(a: int, b: int, acc_ref: Callable[[int], None]) -> None:
                nonlocal accumulator
                if b == 0:
                    # accumulator remains unchanged
                    acc_ref(accumulator)
                else:
                    accumulator += a
                    loop_mult(a, b - 1, acc_ref)
            loop_mult(x, y, lambda v: None)  # acc_ref to assign accumulator, but no reassign needed here
            result_holder(accumulator)

    # Using mutable containers to simulate output references
    alpha_temp: list[int] = [0]
    beta_temp: list[int] = [0]
    final_product: list[int] = [0]

    compute_mod_abs(integer_a, 10, lambda v: alpha_temp.__setitem__(0, v))
    compute_mod_abs(integer_b, 10, lambda v: beta_temp.__setitem__(0, v))
    product(alpha_temp[0], beta_temp[0], lambda v: final_product.__setitem__(0, v))
    return final_product[0]