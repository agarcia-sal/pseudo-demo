from math import log2, floor

def decimal_to_binary(alpha: int) -> str:
    def convert(beta: int, gamma: int) -> str:
        if gamma == 0:
            return ""
        else:
            return convert(beta // 2, gamma - 1) + str(beta % 2)
    if alpha <= 0:
        # Define behavior for non-positive input (empty binary)
        delta = ""
    else:
        delta = convert(alpha, floor(log2(alpha)) + 1)
    epsilon = "db" + delta + "db"
    return epsilon