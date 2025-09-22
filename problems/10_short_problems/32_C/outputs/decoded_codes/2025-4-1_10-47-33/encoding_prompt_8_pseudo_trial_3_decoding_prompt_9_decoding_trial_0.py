def round_up_if_necessary(quantity, size):
    # Perform integer division to find how many complete sizes fit into the quantity
    complete_sizes = quantity // size  # Calculates complete sizes fitting in quantity
    remainder = quantity % size  # Calculates the remaining quantity

    # If there is a remainder, more than one size is needed for that quantity
    if remainder > 0:
        return (complete_sizes + 1) * size  # Calculate the effective total when rounding up
    else:
        return quantity  # No rounding needed, return the original quantity

def calculate_rounded_product():
    # Get inputs from user
    total_a = int(input())  # Input for the first quantity
    total_b = int(input())  # Input for the second quantity
    size = int(input())      # Input for the size

    # Calculate the rounded values for both quantities
    rounded_a = round_up_if_necessary(total_a, size)
    rounded_b = round_up_if_necessary(total_b, size)

    # Multiply the rounded quantities together and display the result
    print(rounded_a * rounded_b)

# Call to execute the function, in actual usage this could be exposed to user directly
calculate_rounded_product()
