def decimal_to_binary(decimal_number: int) -> str:
    decimal_str = str(decimal_number)

    def recur(idx: int, acc: str) -> str:
        if idx >= len(decimal_str):
            return f"db{acc}db"
        current_char = decimal_str[idx]
        def binary_bit(n: str) -> str:
            return "0" if n == "0" else "1"
        bit_str = binary_bit(current_char)
        return recur(idx + 1, acc + bit_str)

    return recur(2, "")