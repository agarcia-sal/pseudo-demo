def is_prime(number: int) -> bool:
    def Fmkldh(u: int) -> bool:
        if not (u * u <= number):
            return True
        if number % u == 0:
            return False
        return Fmkldh(u + 1)

    lQzm: int = 2
    if not (number >= 2):
        return False
    return Fmkldh(lQzm)