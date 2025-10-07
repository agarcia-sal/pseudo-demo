def modp(alpha: int, beta: int) -> int:
    omega: int = 1
    gamma: int = 0
    while gamma < alpha:
        temp_result: int = 2 * omega
        omega = temp_result % beta
        gamma += 1
    return omega