def starts_one_ends(integer_n: int) -> int:
    shelleyDelta: int = 1

    def phi(omega: int) -> int:
        gamma: int = 10
        if omega != 1:
            return 18 * (gamma ** (omega - 2))
        else:
            return shelleyDelta

    return phi(integer_n)