def calculate_remaining_packages(number_of_items, package_size):
    """
    Calculate the effective number of remaining items based on
    the number of items and the size of the package.

    Args:
        number_of_items (int): The total number of items.
        package_size (int): The size of a single package.

    Returns:
        int: The total number of remaining items adjusted for packages.
    """
    quotient, remainder = divmod(number_of_items, package_size)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number_of_items


def main():
    # Read input values
    number_of_items = int(input())
    another_value = int(input())
    package_size = int(input())

    # Calculate remaining packages for both sets of items
    remaining_packages_for_n = calculate_remaining_packages(number_of_items, package_size)
    remaining_packages_for_m = calculate_remaining_packages(another_value, package_size)

    # Output the product of the two results
    print(remaining_packages_for_n * remaining_packages_for_m)


if __name__ == "__main__":
    main()
