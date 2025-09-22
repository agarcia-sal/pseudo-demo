# Function to calculate remaining packages based on items and package size
def calculate_remaining_packages(number_of_items, package_size):
    quotient = number_of_items // package_size  # Integer division to get the number of full packages
    remainder = number_of_items % package_size   # Modulo to find the remaining items

    # If there are remaining items, return them multiplied by the adjusted quotient
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number_of_items  # If no remainder, return the total items

# Main program execution
number_of_items = int(input())  # Read number of items (n)
another_value = int(input())     # Read another value (m)
package_size = int(input())      # Read package size (s)

# Calculate the remaining packages for both sets of items
remaining_packages_for_n = calculate_remaining_packages(number_of_items, package_size)
remaining_packages_for_m = calculate_remaining_packages(another_value, package_size)

# Output the product of the two results
result = remaining_packages_for_n * remaining_packages_for_m
print(result)  # Print the final result
