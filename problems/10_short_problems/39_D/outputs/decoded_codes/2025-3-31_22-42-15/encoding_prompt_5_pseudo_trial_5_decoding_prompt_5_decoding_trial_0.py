# Define the main function to compare two sequences of three integers
def compare_sequences():
    # Step 1: Accept input for two sequences
    print("Enter first sequence of three integers:")
    first_sequence = input()  # Read the first sequence of integers
    print("Enter second sequence of three integers:")
    second_sequence = input()  # Read the second sequence of integers

    # Step 2: Split the input strings into lists of integers
    first_list = list(map(int, first_sequence.split()))  # Convert to list of integers
    second_list = list(map(int, second_sequence.split()))  # Convert to list of integers

    # Step 3: Initialize a counter for differences
    difference_count = 0 

    # Step 4: Compare integers in both lists
    for index in range(3):  # Looping over indices 0 to 2
        first_number = first_list[index]  # Get the first number
        second_number = second_list[index]  # Get the second number
        
        # Step 5: If numbers are different, increment the counter
        if first_number != second_number:  # Check for difference
            difference_count += 1  # Increment the difference count

    # Step 6: Determine if the difference count is less than three
    if difference_count < 3:  # Check if fewer than three differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Call the main function
compare_sequences()
