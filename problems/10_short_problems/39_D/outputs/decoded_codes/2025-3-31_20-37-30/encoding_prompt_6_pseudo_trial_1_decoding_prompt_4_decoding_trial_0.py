def do_main():
    # Step 1: Get input from the user
    first_input = input()
    second_input = input()

    # Step 2: Split the input strings into lists of numbers
    first_numbers = first_input.split()
    second_numbers = second_input.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0 

    # Step 4: Compare corresponding elements of the two number lists
    for index in range(3):
        # Convert string to integer for comparison
        first_number = int(first_numbers[index])
        second_number = int(second_numbers[index])

        # Check if the numbers are different
        if first_number != second_number:
            difference_count += 1 
    
    # Step 5: Output result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()
