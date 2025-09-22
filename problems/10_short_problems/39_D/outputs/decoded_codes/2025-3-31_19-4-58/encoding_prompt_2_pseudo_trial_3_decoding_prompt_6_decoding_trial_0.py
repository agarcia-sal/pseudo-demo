# Start of Program

def do_main():
    # Step 2: Prompt the user to enter the first sequence of numbers
    first_input = input()
    # Step 2: Prompt the user to enter the second sequence of numbers
    second_input = input()

    # Step 3: Split Input Sequences into lists
    first_list = first_input.split()
    second_list = second_input.split()

    # Step 4: Initialize Difference Counter
    difference_count = 0

    # Step 5: Compare Corresponding Numbers for the first three numbers
    for i in range(min(3, len(first_list), len(second_list))):
        first_number = int(first_list[i])  # Convert to integer
        second_number = int(second_list[i])  # Convert to integer
        
        # If the numbers are different, increase the difference count
        if first_number != second_number:
            difference_count += 1

    # Step 6: Check the Difference Count and output the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Main Program Execution
do_main()
