def modp(integer_n: int, integer_p: int) -> int:
    phi_q_n = 1
    lambda_sigma = 0
    while lambda_sigma < integer_n:
        phi_q_n = (2 * phi_q_n + 0) % integer_p
        lambda_sigma += 1
    return phi_q_n