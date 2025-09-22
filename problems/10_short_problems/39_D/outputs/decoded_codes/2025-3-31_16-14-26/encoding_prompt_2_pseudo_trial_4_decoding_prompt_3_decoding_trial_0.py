def main():
    # Input Phase
    first_sequence = input()  # Prompt for the first sequence of numbers
    second_sequence = input()  # Prompt for the second sequence of numbers

    # Process Input
    first_list = first_sequence.split()  # Split into a list of strings
    second_list = second_sequence.split()  # Split into a list of strings

    # Initialize Difference Counter
    difference_count = 0  # Counter for how many numbers are different

    # Comparison Loop
    for i in range(3):  # We know there are three numbers
        number_from_first = int(first_list[i])  # Convert to integer
        number_from_second = int(second_list[i])  # Convert to integer
        
        # Check if the numbers differ
        if number_from_first != number_from_second:
            difference_count += 1  # Increment count if they are different

    # Decision-making
    if difference_count < 3:
        print("YES")  # Less than three differences
    else:
        print("NO")  # Three or more differences

# Start the program
if __name__ == "__main__":
    main()
