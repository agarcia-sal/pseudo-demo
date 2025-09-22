def calculate_remainder_using_division(dividend, divisor):
    # Calculate quotient and remainder
    quotient, remainder = divmod(dividend, divisor)
    
    # Decide the return value based on the remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend

def main():
    # Read inputs
    quantity_a = int(input())
    quantity_b = int(input())
    size = int(input())
    
    # Calculate results based on the two quantities and the size
    result_a = calculate_remainder_using_division(quantity_a, size)
    result_b = calculate_remainder_using_division(quantity_b, size)
    
    # Calculate final result as the product of two results
    final_result = result_a * result_b
    
    # Print the final result
    print(final_result)

# Execute the main function
if __name__ == "__main__":
    main()
