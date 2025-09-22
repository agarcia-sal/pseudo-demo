def normalize_file_path():
    # Read the input path from standard input
    file_path = input().strip()
    
    # Normalize the path by replacing multiple slashes with a single slash
    normalized_path = file_path.replace('//', '/')
    
    # Ensure that leading slashes are reduced to a single slash
    while normalized_path.startswith('/'):
        normalized_path = normalized_path[1:]
    
    # Add a single leading slash to the normalized path
    cleaned_path = '/' + normalized_path
    
    # Print the cleaned-up path
    print(cleaned_path)

# Example test cases (you can uncomment to test)
# Input: '///folder///file.txt'   Output: '/folder/file.txt'
# Input: '   //another_folder/   ' Output: '/another_folder/'
# Input: '//singleSlash/'          Output: '/singleSlash/'
