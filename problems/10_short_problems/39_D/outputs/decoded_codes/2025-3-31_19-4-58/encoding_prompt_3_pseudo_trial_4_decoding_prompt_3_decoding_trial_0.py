def main():
    # Read two lines of input representing two sequences of numbers
    first_sequence = input()
    second_sequence = input()
    
    # Split the input strings into lists of strings
    first_list = first_sequence.split()
    second_list = second_sequence.split()
    
    # Initialize a variable to count the number of differences
    difference_count = 0 

    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert the current elements from strings to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Check if the two numbers are different
        if first_number != second_number:
            # Increment the difference count
            difference_count += 1
            
    # Determine whether fewer than 3 differences exist
    if difference_count < 3:
        # If yes, print "YES"
        print("YES")
    else:
        # Otherwise, print "NO"
        print("NO")

# Start the program
main()
