def calculate_remaining_packages(number_of_items, package_size):
    # Calculate the quotient and remainder of dividing number_of_items by package_size
    quotient = number_of_items // package_size
    remainder = number_of_items % package_size
    
    # Check if there's a remainder and calculate remaining packages
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number_of_items

# Main program
if __name__ == "__main__":
    # Read input values for number of items, another value and package size
    number_of_items = int(input())
    another_value = int(input())
    package_size = int(input())
    
    # Calculate the remaining packages for both sets of items
    remaining_packages_for_n = calculate_remaining_packages(number_of_items, package_size)
    remaining_packages_for_m = calculate_remaining_packages(another_value, package_size)
    
    # Output the product of the two results
    print(remaining_packages_for_n * remaining_packages_for_m)
