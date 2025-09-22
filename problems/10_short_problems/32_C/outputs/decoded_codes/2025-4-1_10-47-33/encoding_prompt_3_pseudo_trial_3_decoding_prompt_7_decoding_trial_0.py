def main():
    # Read the input values for total1, total2, and divisor
    total1 = int(input())  # Read first total
    total2 = int(input())  # Read second total
    divisor = int(input())  # Read divisor

    # Calculate the output using the defined formula
    result = calculate_product_of_adjusted_values(total1, divisor) * calculate_product_of_adjusted_values(total2, divisor)
    
    # Output the final result
    print(result)

def calculate_product_of_adjusted_values(total, divisor):
    # Divide total by divisor to get quotient and remainder
    quotient, remainder = divmod(total, divisor)  # Using divmod for direct quotient and remainder

    # If there is a remainder, calculate the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # If there is no remainder, return total as it is
        return total

# This is the entry point of the program
if __name__ == "__main__":
    main()
