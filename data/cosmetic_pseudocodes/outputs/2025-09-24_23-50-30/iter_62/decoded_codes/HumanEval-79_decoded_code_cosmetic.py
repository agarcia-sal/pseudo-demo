def decimal_to_binary(input_value: int) -> str:
    def extract_binary_string(value: str) -> str:
        return value[2:]  # remove '0b' prefix from binary string

    prefix: str = "db"
    suffix: str = "db"
    binary_representation: str = bin(input_value)
    extracted_string: str = extract_binary_string(binary_representation)
    return prefix + extracted_string + suffix