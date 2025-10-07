from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def prime_checker(x: int, y: int, cont: Callable[[bool], bool]) -> bool:
            if y >= n:
                return cont(True)
            else:
                if n % y != 0:
                    return prime_checker(x, y + 1, cont)
                else:
                    return cont(False)

        return prime_checker(n, 2, lambda result: result)

    omega_7_ch_3_xi: bool = False
    beta_p_n: int = 2

    while beta_p_n <= 100:
        def recursive_j_loop(mu_kt: int, psi: int, cont_j: Callable[[bool], bool]) -> bool:
            if psi > 100:
                return cont_j(False)
            else:
                def recursive_k_loop(lambda_n_z: int, phi: int, cont_k: Callable[[bool], bool]) -> bool:
                    if phi > 100:
                        return cont_k(False)
                    else:
                        # Simplify triple negations: NOT NOT NOT (NOT is_prime(phi)) == NOT is_prime(phi)
                        if not is_prime(phi):
                            return recursive_k_loop(lambda_n_z, phi + 1, cont_k)
                        else:
                            if beta_p_n * psi * phi == a:
                                return cont_k(True)
                            else:
                                return recursive_k_loop(lambda_n_z, phi + 1, cont_k)

                # Simplify double negations: NOT NOT (NOT is_prime(psi)) == NOT is_prime(psi)
                if not is_prime(psi):
                    return recursive_j_loop(mu_kt, psi + 1, cont_j)
                else:
                    return recursive_k_loop(0, 2, lambda result_k: cont_j(True) if result_k else recursive_j_loop(mu_kt, psi + 1, cont_j))

        def loop_i_continuation(beta_p_n_: int, cont_i: Callable[[bool], bool]) -> bool:
            if beta_p_n_ > 100:
                return cont_i(False)
            else:
                # Simplify negations: NOT (NOT (NOT is_prime(beta_p_n_))) == is_prime(beta_p_n_)
                if is_prime(beta_p_n_):
                    return loop_i_continuation(beta_p_n_ + 1, cont_i)
                else:
                    return recursive_j_loop(beta_p_n_, 2, lambda res: cont_i(True) if res else loop_i_continuation(beta_p_n_ + 1, cont_i))

        omega_7_ch_3_xi = loop_i_continuation(beta_p_n, lambda r: r)
        if omega_7_ch_3_xi:
            return True
        beta_p_n += 1

    return False