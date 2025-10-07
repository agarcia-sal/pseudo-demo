from typing import List


def unique_digits(alpha: List[int]) -> List[int]:
    beta: List[int] = []
    gamma: int = 0
    while gamma < len(alpha):
        delta: int = alpha[gamma]
        epsilon: int = 0
        zeta: bool = True
        # Check each digit of delta to see if any digit is even
        while True:
            # Extract the digit at position epsilon
            digit: int = (delta // (10 ** epsilon)) % 10
            if digit % 2 == 0:
                zeta = False
            epsilon += 1
            if (delta // (10 ** epsilon)) == 0 or not zeta:
                break
        if zeta:
            beta.append(delta)
        gamma += 1
    eta: List[int] = beta
    # Bubble sort eta in ascending order
    for i in range(len(eta) - 1):
        for j in range(len(eta) - i - 1):
            if eta[j] > eta[j + 1]:
                theta = eta[j]
                eta[j] = eta[j + 1]
                eta[j + 1] = theta
    return eta