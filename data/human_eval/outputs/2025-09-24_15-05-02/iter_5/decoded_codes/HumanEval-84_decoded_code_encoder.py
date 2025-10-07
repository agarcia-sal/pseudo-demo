def solve(N):
    digits_string = str(N)
    digits_list = [int(char) for char in digits_string]
    digits_sum = sum(digits_list)
    binary_representation = bin(digits_sum)
    result = binary_representation[2:]
    return result