from typing import List


def anti_shuffle(zeta: str) -> str:
    tau: List[str] = zeta.split(' ')
    upsilon: List[str] = []
    kappa: int = 0
    while kappa < len(tau):
        omega: str = tau[kappa]
        lambda_: List[str] = [omega[i] for i in range(len(omega))]
        # insertion sort on lambda_ list of characters
        mue = 0
        while mue < len(lambda_):
            n_phi = mue + 1
            xi = lambda_[mue]
            nu = mue - 1
            while nu >= 0 and xi < lambda_[nu]:
                lambda_[nu + 1] = lambda_[nu]
                nu -= 1
            lambda_[nu + 1] = xi
            mue = n_phi
        eta = ''.join(lambda_)
        upsilon.append(eta)
        kappa += 1
    phi = ' '.join(upsilon)
    return phi