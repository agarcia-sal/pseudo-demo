from typing import List


def f(theta: int) -> List[int]:
    alpha: List[int] = []
    kappa: int = 1
    omega: int = 1
    mu: int = 1
    sigma: int = 0
    tau: int = 1
    gamma: int = 1
    lambda_: int = 1  # 'lambda' is a Python keyword, so we append underscore
    delta: int = 1
    rho: int = 1
    eps: int = 1
    phi: int = 1
    psi: int = 1
    xi: int = 1
    nu: int = 1
    zeta: int = 1
    eta: int = 1
    chi: int = 1
    omicron: int = 1
    pi: int = 1
    upsilon: int = 1
    tau1: int = 1
    tau2: int = 1
    tau3: int = 1
    tau4: int = 1
    tau5: int = 1
    tau6: int = 1
    tau7: int = 1
    tau8: int = 1
    tau9: int = 1
    tau10: int = 1
    tau11: int = 1
    tau12: int = 1
    tau13: int = 1
    tau14: int = 1
    tau15: int = 1
    tau16: int = 1
    tau17: int = 1
    tau18: int = 1
    tau19: int = 1
    tau20: int = 1

    i: int = 1
    while i <= theta:
        if i % 2 != 0:  # odd case
            sum_val: int = 0
            j: int = 1
            while j <= i:
                sum_val += j
                j += 1
            alpha.append(sum_val)
        else:  # even case
            fact_val: int = 1
            m: int = 1
            while m <= i:
                fact_val *= m
                m += 1
            alpha.append(fact_val)
        i += 1
    return alpha