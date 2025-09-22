def calculate_remaining_packages(number_of_items, package_size):
    # Calculate the quotient and remainder when dividing
    quotient = number_of_items // package_size
    remainder = number_of_items % package_size
    
    # If there is a remainder, adjust the calculation
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number_of_items

# Begin main program
n = int(input())  # Read the first number of items
m = int(input())  # Read another value
s = int(input())  # Read package size

# Calculate remaining packages for both sets of items
remaining_packages_for_n = calculate_remaining_packages(n, s)
remaining_packages_for_m = calculate_remaining_packages(m, s)

# Output the product of the two results
print(remaining_packages_for_n * remaining_packages_for_m)
