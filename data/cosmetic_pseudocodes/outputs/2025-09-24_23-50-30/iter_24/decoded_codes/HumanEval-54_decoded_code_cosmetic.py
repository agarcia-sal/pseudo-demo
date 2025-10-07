from typing import Sequence


def same_chars(cipher_alpha: Sequence[str], cipher_beta: Sequence[str]) -> bool:
    buffer_gamma: list[str] = []
    buffer_delta: list[str] = []

    for pointer_eta in range(len(cipher_alpha)):
        if cipher_alpha[pointer_eta] not in buffer_gamma:
            buffer_gamma.append(cipher_alpha[pointer_eta])

    for pointer_theta in range(len(cipher_beta)):
        if cipher_beta[pointer_theta] not in buffer_delta:
            buffer_delta.append(cipher_beta[pointer_theta])

    if len(buffer_gamma) != len(buffer_delta):
        return False

    for pointer_iota in range(len(buffer_gamma)):
        found = False
        for pointer_kappa in range(len(buffer_delta)):
            if buffer_gamma[pointer_iota] == buffer_delta[pointer_kappa]:
                found = True
                break
        if not found:
            return False

    return True