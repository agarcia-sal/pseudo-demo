def main():
    # Read the first set of numbers from the user
    first_set = input().split()

    # Read the second set of numbers from the user
    second_set = input().split()

    # Initialize a counter for differences
    difference_count = 0
    
    # Compare the two sets of numbers
    for index in range(3):  # Loop through indices 0 to 2
        # Convert string values to integers for comparison
        number_from_first_set = int(first_set[index])
        number_from_second_set = int(second_set[index])
        
        # Check if the numbers are different
        if number_from_first_set != number_from_second_set:
            difference_count += 1  # Increment the difference counter
            
    # Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")  # The sets differ in fewer than three instances
    else:
        print("NO")  # The sets differ in three or more instances

# Entry point of the program
if __name__ == "__main__":
    main()
