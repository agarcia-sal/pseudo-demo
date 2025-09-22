def calculate_remainder_using_division(dividend, divisor):
    # Calculate quotient and remainder using integer division and modulus
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # If there is a remainder, adjust the result accordingly
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend

def main():
    # Read input values
    quantity_a = int(input())
    quantity_b = int(input())
    size = int(input())
    
    # Calculate results using the helper function
    result_a = calculate_remainder_using_division(quantity_a, size)
    result_b = calculate_remainder_using_division(quantity_b, size)
    
    # Calculate final result by multiplying the two results
    final_result = result_a * result_b
    
    # Print the final result
    print(final_result)

# Entry point of the program
if __name__ == "__main__":
    main()
