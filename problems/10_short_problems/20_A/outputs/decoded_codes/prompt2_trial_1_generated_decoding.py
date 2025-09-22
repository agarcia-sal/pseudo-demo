# Step 1: Start Program

# Step 2: Read Input
input_path = input().strip()  # Read the sequence of characters and remove leading/trailing spaces

# Step 3: Normalize Path
# Normalize the path by replacing multiple slashes with a single slash
normalized_path = []
segments = input_path.split("/")  # Split the path by slashes

for segment in segments:
    if segment:  # Only add non-empty segments
        normalized_path.append(segment)

# Join the segments back into a normalized path
normalized_path = "/" + "/".join(normalized_path)

# Step 4: Modify Path
# If the normalized path starts with one or more slashes, we already have ensured it starts with a single slash

# Step 5: Output Result
print(normalized_path)  # Display the modified file path

# Step 6: End Program
