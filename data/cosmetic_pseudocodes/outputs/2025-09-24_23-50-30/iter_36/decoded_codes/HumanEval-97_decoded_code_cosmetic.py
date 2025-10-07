def multiply(number_x: int, number_y: int) -> int:
    temp1: int = number_x
    temp2: int = number_y
    remainder1: int = 0
    remainder2: int = 0
    product_result: int = 0

    if temp1 < 0:
        temp1 = -temp1

    if temp2 < 0:
        temp2 = -temp2

    # remainder1 is the last digit of temp1
    remainder1 = temp1 - 10 * ((temp1 - (temp1 % 10)) // 10)
    # remainder2 is the last digit of temp2
    remainder2 = temp2 - 10 * ((temp2 - (temp2 % 10)) // 10)

    product_result = remainder1 * remainder2
    return product_result