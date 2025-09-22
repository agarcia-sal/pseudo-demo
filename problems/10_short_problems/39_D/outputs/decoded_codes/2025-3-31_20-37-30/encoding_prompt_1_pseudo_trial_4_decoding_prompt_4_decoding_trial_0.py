def main():
    # Receive Input
    first_input = input()
    second_input = input()

    # Split Inputs
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize Difference Counter
    difference_count = 0

    # Compare Corresponding Elements
    for index in range(3):  # For indices 0 to 2 inclusive
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        if first_value != second_value:
            difference_count += 1  # Increment count if values differ

    # Determine output
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute main function
if __name__ == "__main__":
    main()
