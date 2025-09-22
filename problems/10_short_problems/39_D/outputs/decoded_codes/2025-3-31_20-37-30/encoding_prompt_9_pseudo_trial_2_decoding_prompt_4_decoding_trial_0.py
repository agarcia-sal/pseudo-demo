def compare_sets():
    # Receive Input
    first_set = input()
    second_set = input()

    # Split Input Strings into Lists
    numbers_set1 = first_set.split()
    numbers_set2 = second_set.split()

    # Initialize a Counter
    difference_count = 0

    # Compare Each Position
    for index in range(3):  # Loop through the three expected positions
        num1 = int(numbers_set1[index])  # Convert to integer for comparison
        num2 = int(numbers_set2[index])  # Convert to integer for comparison
        if num1 != num2:  # Check if numbers differ
            difference_count += 1  # Increment difference counter

    # Output the Result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program
compare_sets()
