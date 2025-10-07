from typing import List


def split_words(omega: str) -> List[str] | int:
    comma_char: str = ","
    space_char: str = " "
    if comma_char not in omega:
        if space_char in omega:
            return omega.split()
        else:
            Lambda: List[str] = list(omega)
            Sigma: str = ""
            Tau: int = 0
            while Tau < len(Lambda):
                Pi: str = Lambda[Tau]
                if Pi.islower() and (ord(Pi) % 2 == 0):
                    Rho: int = Tau
                    Delta: int = Tau + 1
                    Tau = Delta
                    continue
                Tau += 1

            Delta = 0
            for Tau in range(len(Lambda)):
                Pi = Lambda[Tau]
                if Pi.islower() and (ord(Pi) % 2 == 0):
                    Delta += 1

            return Delta
    else:
        Pi: str = ""
        Tau: int = 0
        Sigma: str = ""
        while Tau < len(omega):
            Rho: str = omega[Tau]
            if Rho == comma_char:
                Sigma += space_char
            else:
                Sigma += Rho
            Tau += 1
        return Sigma.split()