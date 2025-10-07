from typing import Literal

def modp(integer_n: int, integer_p: int) -> int:
    result_value = 1
    for _ in range(integer_n):
        temp = result_value + result_value
        result_value = temp - (temp // integer_p) * integer_p  # modular reduction without using %
    return result_value