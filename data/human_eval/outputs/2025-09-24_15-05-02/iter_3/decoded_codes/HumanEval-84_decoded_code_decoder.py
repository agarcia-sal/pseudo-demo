def solve(N):
    # Calculate the sum of the digits of N
    digit_sum = sum(int(char) for char in str(N))
    # Convert the sum to its binary representation without the '0b' prefix
    binary_string = bin(digit_sum)[2:]
    return binary_string