def decimal_to_binary(value: int) -> str:
    bitstring = bin(value)
    segment = bitstring[2:]
    return "db" + segment + "db"