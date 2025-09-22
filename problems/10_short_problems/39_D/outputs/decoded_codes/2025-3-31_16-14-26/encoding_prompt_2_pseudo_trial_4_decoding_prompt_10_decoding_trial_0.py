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
    for index in range(3):  # We know there are exactly three numbers to compare
        number_from_first = int(first_list[index])
        number_from_second = int(second_list[index])
        
        if number_from_first != number_from_second:
            difference_count += 1

    # Decision-making
    if difference_count < 3:
        print("YES")  # Sequences differ in less than three positions
    else:
        print("NO")   # Sequences differ in three or more positions

# Execute the main function
if __name__ == "__main__":
    main()
