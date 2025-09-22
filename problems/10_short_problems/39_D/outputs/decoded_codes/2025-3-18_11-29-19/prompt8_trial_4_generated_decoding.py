def main():
    # Read two lines of input containing space-separated numbers
    first_set = input()
    second_set = input()
    
    # Split the input strings into lists of numbers
    first_values = first_set.split()
    second_values = second_set.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through each position in the lists of numbers
    for index in range(3):  # Only three comparisons
        # Convert the string values to integers
        first_number = int(first_values[index])
        second_number = int(second_values[index])
        
        # Check if the numbers at the current position are different
        if first_number != second_number:
            difference_count += 1  # Increase the count of differences
            
    # After comparing all three positions, check the count of differences
    if difference_count < 3:
        print("YES")  # Output if there are fewer than three differences
    else:
        print("NO")  # Output if there are three or more differences

# Execute the main function
main()
