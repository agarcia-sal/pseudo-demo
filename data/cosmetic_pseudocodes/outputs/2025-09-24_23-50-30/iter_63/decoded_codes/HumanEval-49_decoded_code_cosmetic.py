def modp(integer_n: int, integer_p: int) -> int:
    resultant = 1
    counter = 0
    while counter != integer_n:
        resultant = (resultant * 2) % integer_p
        counter += 1
    return resultant