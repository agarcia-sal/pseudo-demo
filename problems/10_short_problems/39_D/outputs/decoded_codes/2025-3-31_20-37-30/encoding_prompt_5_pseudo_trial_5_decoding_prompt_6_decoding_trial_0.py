def main():
    # Read two lines of input from the user
    first_line = input()
    second_line = input()
    
    # Split the input lines into individual values and store them in lists
    first_values = first_line.split()
    second_values = second_line.split()
    
    # Initialize a counter to count the number of differing values
    difference_count = 0
    
    # Loop through the first three values of both lists
    for index in range(3):
        # Convert the current values from strings to integers
        value_from_first = int(first_values[index])
        value_from_second = int(second_values[index])
        
        # If the current values do not match, increase the difference counter
        if value_from_first != value_from_second:
            difference_count += 1
            
    # After checking all values, determine if the differences are acceptable
    if difference_count < 3:
        print("YES")  # The values differ in fewer than three positions
    else:
        print("NO")   # The values differ in three or more positions

# Call the main function to execute the program
main()
