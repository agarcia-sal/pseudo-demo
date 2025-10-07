from typing import Callable


def is_multiply_prime(xq: int) -> bool:
    def is_prime(bw: int) -> bool:
        def loop_prim(yk: int) -> bool:
            if yk >= bw:
                return True
            if bw % yk == 0:
                return False
            return loop_prim(yk + 1)
        return loop_prim(2)

    def loop_i(xv: int) -> bool:
        if xv > 100:
            return False
        if not is_prime(xv):
            return loop_i(xv + 1)

        def loop_j(kp: int) -> bool:
            if kp > 100:
                return loop_i(xv + 1)
            if not is_prime(kp):
                return loop_j(kp + 1)

            def loop_k(uv: int) -> bool:
                if uv > 100:
                    return loop_j(kp + 1)
                if not is_prime(uv):
                    return loop_k(uv + 1)
                if xv * kp * uv == xq:
                    return True
                return loop_k(uv + 1)

            return loop_k(2)

        return loop_j(2)

    return loop_i(2)