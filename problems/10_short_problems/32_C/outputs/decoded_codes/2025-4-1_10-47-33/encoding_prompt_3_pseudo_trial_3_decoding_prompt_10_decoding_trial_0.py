def main():
    # Read the input values for total1, total2, and divisor
    total1 = int(input())
    total2 = int(input())
    divisor = int(input())
    
    # Calculate the output using the defined formula
    result = calculate_product_of_adjusted_values(total1, divisor) * calculate_product_of_adjusted_values(total2, divisor)
    
    # Output the result
    print(result)

def calculate_product_of_adjusted_values(total, divisor):
    # Calculate the quotient and remainder using integer division
    quotient, remainder = divmod(total, divisor)
    
    # If there is a remainder, calculate the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # If there is no remainder, return total as it is
        return total

# This is the entry point of the program
if __name__ == "__main__":
    main()
