def normalize_file_path(path):
    # Replace backslashes with slashes for consistency
    path = path.replace('\\', '/')
    
    # Normalize the path: split it by slashes, filter empty segments, and then join them back
    segments = path.split('/')
    filtered_segments = [segment for segment in segments if segment]
    normalized_path = '/' + '/'.join(filtered_segments)
    
    return normalized_path

# Step 1: Receive Input
input_path = input().strip()  # Read input from standard input and remove surrounding whitespace

# Step 2: Normalize the File Path
normalized_path = normalize_file_path(input_path)

# Step 3: Output the Result
print(normalized_path)
