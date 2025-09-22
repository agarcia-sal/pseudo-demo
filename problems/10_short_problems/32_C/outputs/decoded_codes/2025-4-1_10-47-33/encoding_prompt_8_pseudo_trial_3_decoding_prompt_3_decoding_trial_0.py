def calculate_rounded_product():
    # Define a function to calculate rounded quantity
    def round_up_if_necessary(quantity, size):
        # Perform integer division to find how many complete sizes fit in the quantity
        complete_sizes = quantity // size
        remainder = quantity % size
        
        # If there is a remainder, more than one size is needed for that quantity 
        if remainder > 0:
            return (complete_sizes + 1) * size  # Calculate the effective total when rounding up
        else:
            return quantity  # No rounding needed, return the original quantity
    
    # Get inputs from user
    total_a = int(input())
    total_b = int(input())
    size = int(input())
    
    # Calculate the rounded values for both quantities
    rounded_a = round_up_if_necessary(total_a, size)
    rounded_b = round_up_if_necessary(total_b, size)
    
    # Multiply the rounded quantities together and display the result
    print(rounded_a * rounded_b)

# Call the function to execute
calculate_rounded_product()
