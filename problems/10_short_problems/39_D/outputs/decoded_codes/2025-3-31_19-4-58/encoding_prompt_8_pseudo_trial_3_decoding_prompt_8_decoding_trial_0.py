def main():
    # Read two lines of input from the user
    inputLine1 = input()
    inputLine2 = input()
    
    # Split input lines into lists of strings
    list1 = inputLine1.split()
    list2 = inputLine2.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the corresponding elements to integers
        valueA = int(list1[index])
        valueB = int(list2[index])
        
        # Check if the two values are different
        if valueA != valueB:
            # Increment the difference counter
            differenceCount += 1
            
    # Determine the final output based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
main()


     1 2 3
     1 2 3
     

     1 2 3
     4 2 3
     

     1 2 3
     4 5 3
     

     1 2 3
     4 5 6
     

     0 0 0
     0 0 1
     

     1000 2000 3000
     1000 2000 4000
     