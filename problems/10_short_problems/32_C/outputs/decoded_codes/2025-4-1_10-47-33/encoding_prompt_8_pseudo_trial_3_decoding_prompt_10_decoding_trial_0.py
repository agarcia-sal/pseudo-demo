def calculate_rounded_product():
    """Calculate the product of two quantities after rounding up based on a given size."""
    
    def round_up_if_necessary(quantity, size):
        """
        Round up the quantity based on size. If the quantity is not a complete
        multiple of size, the function returns the next complete multiple.
        
        Parameters:
            quantity (int): The quantity to round.
            size (int): The size to use for rounding.
        
        Returns:
            int: Adjusted quantity after rounding.
        """
        complete_sizes = quantity // size
        remainder = quantity % size
        
        if remainder > 0:
            return (complete_sizes + 1) * size  # Round up
        else:
            return quantity  # No rounding needed

    # Get inputs from user
    total_a = int(input())
    total_b = int(input())
    size = int(input())
    
    # Calculate the rounded values for both quantities
    rounded_a = round_up_if_necessary(total_a, size)
    rounded_b = round_up_if_necessary(total_b, size)

    # Multiply the rounded quantities together and display the result
    print(rounded_a * rounded_b)

# Calling the function to execute
calculate_rounded_product()
