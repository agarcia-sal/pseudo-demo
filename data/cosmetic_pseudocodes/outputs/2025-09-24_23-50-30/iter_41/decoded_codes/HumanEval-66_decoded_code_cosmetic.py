def digitSum(omega: str) -> int:
    if omega == "":
        return 0
    epsilon = 0
    for delta in omega:
        # Add ASCII of delta if delta is uppercase letter A-Z
        epsilon += ord(delta) if "A" <= delta <= "Z" else 0
    return epsilon