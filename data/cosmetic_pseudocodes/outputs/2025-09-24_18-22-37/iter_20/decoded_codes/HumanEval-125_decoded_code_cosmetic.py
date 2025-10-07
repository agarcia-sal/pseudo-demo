from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    delta: int = 0
    if " " in text:
        return text.split()
    else:
        if "," in text:
            sigma: str = ""
            psi: int = 0  # zero-based index
            tau: int = len(text)
            while psi < tau:
                if text[psi] == ",":
                    sigma += " "
                else:
                    sigma += text[psi]
                psi += 1
            return sigma.split()
        else:
            omega: List[str] = []
            rho: int = 0  # zero-based index
            length: int = len(text)
            while rho < length:
                nu: str = text[rho]
                xi: int = ord(nu) % 2
                if "a" <= nu <= "z" and xi == 0:
                    omega.append(nu)
                rho += 1
            delta = len(omega)
            return delta