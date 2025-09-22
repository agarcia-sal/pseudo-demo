def main():
    # Step 1: Gather input from the user
    print("Enter the first set of numbers, separated by spaces:")
    first_set = input()
    
    print("Enter the second set of numbers, separated by spaces:")
    second_set = input()
    
    # Step 2: Split the input strings into lists of numbers
    numbers_from_first_set = first_set.split()
    numbers_from_second_set = second_set.split()
    
    # Step 3: Initialize the difference counter
    difference_count = 0 
    
    # Step 4: Compare corresponding numbers from both sets
    for position in range(3):  # We expect only 3 numbers in each set
        # Convert the current pair of strings to integers
        first_number = int(numbers_from_first_set[position])
        second_number = int(numbers_from_second_set[position])
        
        # Check if the numbers are different
        if first_number != second_number:
            difference_count += 1
            
    # Step 5: Determine the output based on the difference count
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
