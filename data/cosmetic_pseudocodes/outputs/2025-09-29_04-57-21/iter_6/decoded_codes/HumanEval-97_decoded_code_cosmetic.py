def multiply(num_x: int, num_y: int) -> int:
    val1 = num_x
    while val1 < 0:
        val1 += 10
    val1 = val1 - ((val1 // 10) * 10)

    val2 = num_y
    while val2 < 0:
        val2 += 10
    val2 = val2 - ((val2 // 10) * 10)

    return val1 * val2