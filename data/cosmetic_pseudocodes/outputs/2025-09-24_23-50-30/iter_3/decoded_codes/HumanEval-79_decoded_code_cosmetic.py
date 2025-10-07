def decimal_to_binary(num: int) -> str:
    binary_str: str = bin(num)  # Python's bin returns string like '0b101'
    output: str = "db" + binary_str[1:] + "db"  # slice from index 1 to get 'bxxx...'
    return output