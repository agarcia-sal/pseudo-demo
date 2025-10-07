def decimal_to_binary(decimal_number: int) -> str:
    bits = ""
    n = decimal_number
    while n != 0:
        bits = str(n % 2) + bits
        n //= 2
    if bits == "":
        bits = "0"
    return "db" + bits + "db"