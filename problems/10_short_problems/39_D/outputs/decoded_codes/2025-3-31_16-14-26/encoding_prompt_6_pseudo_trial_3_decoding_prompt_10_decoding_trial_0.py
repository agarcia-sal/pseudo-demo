def main():
    # Read input values from the user
    first_string = input()
    second_string = input()
    
    # Split the input strings into lists of items
    first_list = first_string.split()
    second_list = second_string.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements from both lists to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Compare the two values
        if first_value != second_value:
            # If they are different, increment the difference counter
            difference_count += 1
    
    # Check the count of differences
    if difference_count < 3:
        # If there are fewer than 3 differences, print "YES"
        print("YES")
    else:
        # Otherwise, print "NO"
        print("NO")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()


   1 2 3
   1 2 3
   

   1 2 3
   1 2 4
   

   5 5 5
   1 2 3
   

   9 8 7
   9 7 6
   

   1 3 4
   1 3 4
   