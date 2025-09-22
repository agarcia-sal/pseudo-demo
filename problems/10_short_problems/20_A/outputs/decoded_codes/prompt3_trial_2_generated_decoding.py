def main():
    # Read input from the standard input stream
    raw_path = input()
    
    # Normalize the path by removing any unnecessary segments
    normalized_path = normalize_path(raw_path)
    
    # Clean the normalized path by ensuring it starts with a single forward slash
    cleaned_path = replace_multiple_leading_slashes(normalized_path)

    # Print the final cleaned path
    print(cleaned_path)

def normalize_path(path):
    # Replace backward slashes with forward slashes
    path = path.replace('\\', '/')
    
    # Split the path into segments and handle normalization of segments
    segments = path.split('/')
    simplified_segments = []
    
    for segment in segments:
        if segment == '' or segment == '.':
            continue  # Skip empty or current directory indicators
        elif segment == '..':
            if simplified_segments:
                simplified_segments.pop()  # Go up one directory level if possible
        else:
            simplified_segments.append(segment)  # Add valid segments

    # Join the normalized segments back into a cleaned path
    simplified_path = '/'.join(simplified_segments)
    
    return simplified_path

def replace_multiple_leading_slashes(path):
    # Check for leading slashes and replace multiple with a single slash
    if path.startswith('//'):
        return '/' + path.lstrip('/')
    return path

# Call the main function to execute the program
if __name__ == "__main__":
    main()
