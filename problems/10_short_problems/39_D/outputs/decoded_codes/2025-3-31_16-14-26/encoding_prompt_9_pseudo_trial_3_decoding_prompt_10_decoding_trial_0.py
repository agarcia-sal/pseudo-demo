def main():
    # Prompt the user for input and read two lines of numeric values
    first_sequence = input().split()
    second_sequence = input().split()

    # Initialize a variable to count differences
    difference_count = 0

    # Compare corresponding values in the two sequences
    for index in range(3):
        first_value = int(first_sequence[index])
        second_value = int(second_sequence[index])
        
        # Increment the difference count for unequal values
        if first_value != second_value:
            difference_count += 1

    # Determine and print the output based on the differences count
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
if __name__ == "__main__":
    main()
