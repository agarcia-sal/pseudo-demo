def absolute_value(num):
    """Return the absolute value of the input number."""
    if num < 0:
        return -num
    return num

def sum_of_first_i_numbers(i):
    """Return the sum of the first i natural numbers."""
    return (i * (i + 1)) // 2  # Use integer division for accurate results

def find_natural_number(n):
    """Find and return the minimum natural number whose sum of first 'i' numbers
    equals or exceeds the absolute value of 'n' in a specific manner."""
    n = absolute_value(n)  # Take the absolute value of the input number
    i = 0  # Initialize the counter for natural numbers

    while True:  # Infinite loop to find the required number
        s = sum_of_first_i_numbers(i)  # Calculate the sum of the first i natural numbers
        m = s - n  # Calculate how much s exceeds n

        if s == n:  # Check if the sum equals n
            return i  # Return the current number i

        elif s > n:  # Check if the sum exceeds n
            if m % 2 == 0:  # Check if the difference m is even
                return i  # Return the current number i

        i += 1  # Increment i for the next iteration

# Read input from the user
n = int(input())
result = find_natural_number(n)  # Call the function and store the result
print(result)  # Print the result
