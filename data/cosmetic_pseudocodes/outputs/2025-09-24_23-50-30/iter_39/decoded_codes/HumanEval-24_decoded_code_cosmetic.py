def largest_divisor(omega: int) -> int:
    psi = omega - 1
    while psi > 0:
        if omega - ((omega // psi) * psi) == 0:
            return psi
        psi -= 1
    # If no divisor found (outside problem domain), return 1 as smallest divisor
    return 1