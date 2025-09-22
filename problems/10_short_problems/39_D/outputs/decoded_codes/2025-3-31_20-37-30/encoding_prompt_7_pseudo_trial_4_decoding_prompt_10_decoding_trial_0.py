def main():
    # Read two strings from user input
    string1 = input()
    string2 = input()
    
    # Split the input strings into lists of substrings
    list1 = string1.split()
    list2 = string2.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Compare the first three elements of both lists
    for index in range(3):  # Assuming the input is always valid with at least 3 elements
        # Convert list elements to integers for comparison
        value_from_list1 = int(list1[index])
        value_from_list2 = int(list2[index])
        
        # Check if the values are different
        if value_from_list1 != value_from_list2:
            difference_count += 1
    
    # Determine if less than three differences were found
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
if __name__ == "__main__":
    main()


     1 2 3
     1 2 3
     

     1 2 3
     1 4 3
     

     1 2 3
     4 5 6
     

     1 1 1
     2 2 2
     