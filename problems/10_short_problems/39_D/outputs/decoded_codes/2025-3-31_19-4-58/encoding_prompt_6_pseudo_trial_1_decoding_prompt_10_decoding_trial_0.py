def main_procedure():
    # Read the first line of input and store it as string1
    string1 = input()
    
    # Read the second line of input and store it as string2
    string2 = input()
    
    # Split each input string into a list of strings
    list1 = string1.split()
    list2 = string2.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the first three elements of each list
    for index in range(3):
        # Convert the current elements to integers
        number_from_list1 = int(list1[index])
        number_from_list2 = int(list2[index])
        
        # Check if the two numbers are different
        if number_from_list1 != number_from_list2:
            # Increment the difference counter
            difference_count += 1
    
    # If the count of differences is less than 3, print "YES"
    if difference_count < 3:
        print("YES")
    else:
        # If the count of differences is 3 or more, print "NO"
        print("NO")

# Start the program by calling the main_procedure
if __name__ == "__main__":
    main_procedure()
