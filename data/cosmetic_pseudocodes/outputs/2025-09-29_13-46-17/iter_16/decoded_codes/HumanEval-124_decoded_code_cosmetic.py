import re
from typing import Callable, Tuple


def valid_date(date_string: str) -> bool:
    def _func(head: str, y: str) -> Tuple[str, str]:
        if head != '-':
            return y, head
        else:
            return y + head, ''

    def _zeta(lambda_: str, mu: str, nu: str, rho: str) -> Tuple[str, str, str]:
        if rho == '':
            return lambda_, mu, nu
        else:
            a, b = _func(rho[0], rho[1:])
            if a == '':
                return _zeta(mu, nu, '', b)
            else:
                return _zeta(lambda_ + a, mu, nu, b)

    def _phi(s: str) -> str:
        match = re.match(r'^\s*(.*?)\s*$', s)
        return match.group(1) if match else ''

    def _iota(sigma: str) -> int:
        length: int = len(sigma)

        def kappa(i: int, acc: int) -> int:
            if i >= length:
                return acc
            elif '0' <= sigma[i] <= '9':
                return kappa(i + 1, acc * 10 + (ord(sigma[i]) - ord('0')))
            else:
                raise ValueError('Non-digit character encountered')

        return kappa(0, 0)

    def _rho(lambda_: int, mu: int, nu: int) -> bool:
        if lambda_ < 1 or lambda_ > 12:
            return False
        elif lambda_ in {1, 3, 5, 7, 8, 10, 12}:
            if mu < 1 or mu > 31:
                return False
            else:
                return _rho_SER(nu)
        elif lambda_ in {4, 6, 9, 11}:
            if mu < 1 or mu > 30:
                return False
            else:
                return _rho_SER(nu)
        elif lambda_ == 2:
            if mu < 1 or mu > 29:
                return False
            else:
                return _rho_SER(nu)
        else:
            return False

    def _rho_SER(sigma: int) -> bool:
        return True

    def _epsilon() -> bool:
        p_str = _phi(date_string)
        alpha, beta, gamma = _zeta('', '', '', p_str)
        M = _iota(alpha)
        D = _iota(beta)
        Y = _iota(gamma)
        return _rho(M, D, Y)

    def _epsilon_CPS(cont: Callable[[], bool]) -> bool:
        try:
            return cont()
        except Exception:
            return False

    return _epsilon_CPS(_epsilon)