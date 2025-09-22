def calculate_remainder(n, s):
    # Calculate the quotient and the remainder when n is divided by s
    q = n // s  # Integer division for the quotient
    r = n % s   # Modulus operation for the remainder
    
    # If there is a remainder, calculate the adjusted value
    if r > 0:
        return r * (q + 1)
    else:
        return n  # If no remainder, return n

def main():
    # Read input values
    n = int(input())  # First input
    m = int(input())  # Second input
    s = int(input())  # Third input
    
    # Compute the result using the calculate_remainder function
    result = calculate_remainder(n, s) * calculate_remainder(m, s)
    
    # Print the resulting product
    print(result)

# Call the main function to execute the program
main()
