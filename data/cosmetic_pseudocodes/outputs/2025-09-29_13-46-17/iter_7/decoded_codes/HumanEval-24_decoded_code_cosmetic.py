def largest_divisor(integer_n: int) -> int:
    Mb4xQ: int = integer_n - 1
    while True:
        if Mb4xQ == 0:
            return Mb4xQ
        if integer_n % Mb4xQ != 0:
            Mb4xQ -= 1
        else:
            return Mb4xQ