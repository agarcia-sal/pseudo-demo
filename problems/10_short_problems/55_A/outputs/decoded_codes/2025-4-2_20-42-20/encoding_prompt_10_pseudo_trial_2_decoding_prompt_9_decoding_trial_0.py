# Start of the program

# Input: Get an integer n from the user
n = int(input())

# Initialize an array b of size n with all values set to True
b = [True] * n

# Initialize index j to 0
j = 0

# Initialize step i to 1
i = 1

# While i is less than or equal to 500000 do:
while i <= 500000:
    # If b[j] is True then:
    if b[j]:
        # Set b[j] to False
        b[j] = False
    
    # Increment i by 1
    i += 1
    
    # Update j to (j + i) modulo n
    j = (j + i) % n

# Create an array x to store elements from b that are still True
x = [value for value in b if value]

# If the size of x is 0 then:
if len(x) == 0:
    # Output "YES"
    print("YES")
else:
    # Else output "NO"
    print("NO")

# End of the program
