def main():
    # Step 1: Accept input for two sequences
    print("Enter first sequence of three integers:")
    first_sequence = input()
    print("Enter second sequence of three integers:")
    second_sequence = input()

    # Step 2: Split the input strings into lists of integers
    first_list = [int(num) for num in first_sequence.split()]
    second_list = [int(num) for num in second_sequence.split()]

    # Step 3: Initialize a counter for differences
    difference_count = 0 

    # Step 4: Compare integers in both lists
    for index in range(3):
        first_number = first_list[index]
        second_number = second_list[index]

        # Step 5: If numbers are different, increment the counter
        if first_number != second_number:
            difference_count += 1 

    # Step 6: Determine if the difference count is less than three
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Ensure the main function is called
if __name__ == "__main__":
    main()
