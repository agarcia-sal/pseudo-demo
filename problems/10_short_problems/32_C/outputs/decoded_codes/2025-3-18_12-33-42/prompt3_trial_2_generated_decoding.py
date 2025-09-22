def main():
    # Read input values for total_units and multiplier
    total_units = int(input())
    multiplier = int(input())
    increment_size = int(input())
    
    # Calculate the result using helper function compute_increment
    result = compute_increment(total_units, increment_size) * compute_increment(multiplier, increment_size)
    
    # Output the final result
    print(result)

def compute_increment(units, size):
    # Divide units by size to get the quotient and remainder
    quotient, remainder = divmod(units, size)

    # If there is a remainder, calculate using the formula
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return units

# Call the main function to execute the program
main()
