def main():
    # Read input from the user
    first_string = input()
    second_string = input()
    
    # Split the input strings into lists of strings
    first_list = first_string.split()
    second_list = second_string.split()
    
    # Initialize a variable to count differences
    difference_count = 0
    
    # Loop through each corresponding element in both lists
    for index in range(3): 
        # Convert the elements to integers for comparison
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the two values are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1
    
    # If the number of differences is less than 3, print "YES"
    if difference_count < 3:
        print("YES")
    else:
        # Otherwise, print "NO"
        print("NO")

# Entry point of the program
main()
