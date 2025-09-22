def calculate_rounded_product():
    # Function to round up the quantity based on the size
    def round_up_if_necessary(quantity, size):
        # Perform integer division to find how many complete sizes fit in the quantity
        complete_sizes = quantity // size
        remainder = quantity % size
        
        # If there is a remainder, we need to round up
        if remainder > 0:
            return (complete_sizes + 1) * size  # Return the effective total when rounding up
        else:
            return quantity  # No rounding needed, return the original quantity

    # Get inputs from user
    total_a = int(input())  # First quantity
    total_b = int(input())  # Second quantity
    size = int(input())      # Size to round up against

    # Calculate the rounded values for both quantities
    rounded_a = round_up_if_necessary(total_a, size)
    rounded_b = round_up_if_necessary(total_b, size)

    # Multiply the rounded quantities together and display the result
    print(rounded_a * rounded_b)

# Example test inputs could be:
# total_a = 5, total_b = 3, size = 2  -> Output should be 18 (6 * 3)
# total_a = 7, total_b = 4, size = 5  -> Output should be 20 (10 * 2)
