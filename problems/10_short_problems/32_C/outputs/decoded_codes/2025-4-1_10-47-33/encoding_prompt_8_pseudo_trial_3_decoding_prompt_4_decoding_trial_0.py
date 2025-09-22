def calculate_rounded_product():
    # Function to round up the quantity based on the size
    def round_up_if_necessary(quantity, size):
        complete_sizes = quantity // size
        remainder = quantity % size
        
        # Calculate the effective total when rounding up
        if remainder > 0:
            return (complete_sizes + 1) * size  # Return the next complete size
        else:
            return quantity  # No rounding needed

    # Get inputs from the user
    total_a = int(input())
    total_b = int(input())
    size = int(input())
    
    # Calculate the rounded values for both quantities
    rounded_a = round_up_if_necessary(total_a, size)
    rounded_b = round_up_if_necessary(total_b, size)

    # Multiply the rounded quantities together and print the result
    print(rounded_a * rounded_b)

# Call the function to execute
calculate_rounded_product()
