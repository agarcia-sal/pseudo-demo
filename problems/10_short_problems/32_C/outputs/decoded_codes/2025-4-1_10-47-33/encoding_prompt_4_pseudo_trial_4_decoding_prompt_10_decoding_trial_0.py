def mc(number, size):
    """Calculate a modified value based on the input number and size."""
    quotient, remainder = divmod(number, size)  # Divide number by size to get quotient and remainder
    if remainder > 0:
        return remainder * (quotient + 1)  # Adjust value if remainder exists
    else:
        return number  # Return original number if no remainder

def main():
    """Main function to read input values and calculate the result."""
    # Read input values
    n = int(input())
    m = int(input())
    s = int(input())

    # Calculate result using the 'mc' function for both n and m
    result = mc(n, s) * mc(m, s)

    # Output the result
    print(result)

if __name__ == "__main__":
    main()
