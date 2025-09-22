def main():
    # Input Phase
    first_sequence = input()
    second_sequence = input()

    # Process Input
    first_list = first_sequence.split()
    second_list = second_sequence.split()

    # Initialize Difference Counter
    difference_count = 0

    # Comparison Loop
    for i in range(3):  # We know there are always 3 numbers based on the prompt
        number_from_first = int(first_list[i])
        number_from_second = int(second_list[i])
        
        # Checking if the numbers at the same position are different
        if number_from_first != number_from_second:
            difference_count += 1

    # Decision-making
    if difference_count < 3:
        print("YES")  # The sequences differ in less than three positions
    else:
        print("NO")   # The sequences differ in three or more positions

# The program begins execution here
if __name__ == "__main__":
    main()
