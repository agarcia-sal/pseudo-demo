def main():
    # Prompt the user to input two sets of numbers
    print("Please enter the first set of numbers:")
    first_set = input()
    print("Please enter the second set of numbers:")
    second_set = input()
    
    # Split the input strings into individual numbers
    numbers_from_first_set = first_set.split()
    numbers_from_second_set = second_set.split()
    
    # Initialize a counter for differences
    difference_counter = 0 
    
    # Loop through each pair of corresponding numbers
    for index in range(3):  # Looping from 0 to 2
        # Convert the input strings to integers
        first_number = int(numbers_from_first_set[index])
        second_number = int(numbers_from_second_set[index])
        
        # Compare the numbers and increment the counter if they differ
        if first_number != second_number:
            difference_counter += 1
    
    # Check the number of differences and output the result
    if difference_counter < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
main()
