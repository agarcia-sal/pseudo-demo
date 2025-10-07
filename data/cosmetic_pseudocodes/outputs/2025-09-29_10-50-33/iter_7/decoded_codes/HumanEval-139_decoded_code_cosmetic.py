def special_factorial(number_limit: int) -> int:
    progressive_product: int = 1
    compound_product: int = 1
    iterator: int = 1
    while iterator <= number_limit:
        progressive_product *= iterator
        compound_product *= progressive_product
        iterator += 1
    return compound_product