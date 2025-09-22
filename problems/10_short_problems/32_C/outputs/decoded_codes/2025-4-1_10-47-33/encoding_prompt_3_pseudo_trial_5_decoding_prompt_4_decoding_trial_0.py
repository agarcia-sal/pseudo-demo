def calculate_remaining_packages(number_of_items, package_size):
    quotient = number_of_items // package_size
    remainder = number_of_items % package_size
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number_of_items

def main():
    # Read user input for number of items and package size
    number_of_items = int(input())
    another_value = int(input())
    package_size = int(input())
    
    # Calculate the remaining packages for both sets of items
    remaining_packages_for_n = calculate_remaining_packages(number_of_items, package_size)
    remaining_packages_for_m = calculate_remaining_packages(another_value, package_size)

    # Output the product of the two results
    result = remaining_packages_for_n * remaining_packages_for_m
    print(result)

if __name__ == "__main__":
    main()
