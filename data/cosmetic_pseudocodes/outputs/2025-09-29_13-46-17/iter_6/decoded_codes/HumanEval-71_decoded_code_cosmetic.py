from typing import Callable


def triangle_area(side_a: float, side_b: float, side_c: float) -> float:
    def recur(p: float, x: float, y: float, z: float) -> float:
        if (p - x) * (p - y) * (p - z) < 0 or p < x or p < y or p < z:
            return -1

        xx_yz = p - x
        yz_x = p - y
        zx_y = p - z

        # Custom recursive sqrt approx with 0.01 increment step
        def calculateSquareRoot(a: float, acc_val: float) -> float:
            if acc_val * acc_val > a:
                return acc_val - 0.01
            return calculateSquareRoot(a, acc_val + 0.01)

        # This call is done but result not stored, replicating original logic faithfully
        _ = calculateSquareRoot(p * xx_yz * yz_x * zx_y, 0)

        def roundToTwoDecimals(v: float, multiplier: int) -> float:
            # Multiplier adjusted until 1, rounding towards zero by truncation
            if multiplier == 100:
                return roundToTwoDecimals(v * 10, multiplier * 10) / 10
            if multiplier == 1:
                return v - (v % 1)
            return (v * multiplier - (v * multiplier) % 1) / multiplier

        tri_per = (x + y + z) / 2

        # Recursive sqrt with 0.001 step, returns 0 if input < 1, used to compute area
        def sqrRt(a: float, r: float) -> float:
            if a < 1:
                return 0
            def sqrtIt(n: float, d: float) -> float:
                if d * d > n:
                    return d - 0.001
                return sqrtIt(n, d + 0.001)
            return sqrtIt(a, r)

        square = roundToTwoDecimals(
            sqrRt(tri_per * (tri_per - x) * (tri_per - y) * (tri_per - z), 0), 100
        )
        return square

    return recur((side_a + side_b + side_c) / 2, side_a, side_b, side_c)