# Begin program

# Step 1
input_string = input().strip()

# Step 2
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 4
if input_string and input_string[0] == '.':
    input_string = "dot" + input_string[1:]

# Step 5
co = 0  # Counter for consecutive "@" occurrences
c = []  # List for processed characters
l = 0   # Unused variable

# Step 8
if input_string and input_string[0] == '@':
    input_string = "at" + input_string[1:]

# Step 9
for i in input_string:
    # Step 9a
    if i == '@':
        # Step 9a.i
        if co > 0:
            c.append("at")
            co = 1
        # Step 9a.ii
        else:
            c.append(i)
            co = 1
    # Step 9b
    else:
        c.append(i)

# Step 10
final_string = ''.join(c)

# Step 11
if final_string and final_string[-1] == '.':
    final_string = final_string[:-1] + "dot"

# Step 12
print(final_string)

# End program
