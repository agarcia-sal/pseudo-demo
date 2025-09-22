def main():
    # Read two lines of input for the first and second lists
    first_list = input()
    second_list = input()

    # Split the input strings into lists of values
    first_values = first_list.split()
    second_values = second_list.split()

    # Initialize a counter for differences
    difference_count = 0

    # Loop through each element in the range of 0 to 2 (inclusive)
    for index in range(3):  # We assume both lists have exactly 3 elements
        value_a = int(first_values[index])    # Convert to integer
        value_b = int(second_values[index])    # Convert to integer

        # Increment the difference count if values are not equal
        if value_a != value_b:
            difference_count += 1

    # Output results based on the difference count
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Invoke the main function when the script is executed
if __name__ == "__main__":
    main()
