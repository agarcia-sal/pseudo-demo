def main():
    # Input Phase: Getting two sequences of numbers from the user
    first_sequence = input()
    second_sequence = input()

    # Process Input: Splitting the sequences into lists of strings
    first_list = first_sequence.split()
    second_list = second_sequence.split()

    # Initialize Difference Counter
    difference_count = 0

    # Comparison Loop: Check each number in the sequences
    for i in range(3):
        # Convert strings to integers
        number_from_first = int(first_list[i])
        number_from_second = int(second_list[i])
        
        # Increment the difference counter if the numbers are different
        if number_from_first != number_from_second:
            difference_count += 1

    # Decision-making based on the difference count
    if difference_count < 3:
        print("YES")  # Sequences differ in less than three positions
    else:
        print("NO")   # Sequences differ in three or more positions

# The main function is executed when the program runs
main()
