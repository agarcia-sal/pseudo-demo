import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to read text files from a directory
def read_files_from_directory(directory_path):
    file_contents = []
    file_names = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                file_contents.append(file.read())
                file_names.append(filename)
    return file_contents, file_names


def get_vector_matrix(path_name_1, path_name_2):
    directory_path_1 = path_name_1
    directory_path_2 = path_name_2

    documents_1, filenames_1 = read_files_from_directory(directory_path_1)
    documents_2, filenames_2 = read_files_from_directory(directory_path_2)
    all_documents = documents_1 + documents_2

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit(all_documents)

    # feature_names = vectorizer.get_feature_names_out()


    # Convert the matrix into a more readable format
    # tfidf_data = tfidf_matrix.toarray()

    # Display results for each file
    # for doc_index, doc_name in enumerate(filenames):
    #     print(f"TF-IDF for {doc_name}:")
    #     for word_index, score in enumerate(tfidf_data[doc_index]):
    #         if score > 0:  # Only display words with non-zero scores
    #             print(f"  {feature_names[word_index]}: {score:.4f}")
    #     print("\n")

    tfidf_1 = vectorizer.transform(documents_1)
    tfidf_2 = vectorizer.transform(documents_2)

# Now you can compare tfidf_X and tfidf_Y without dimension mismatch
    cosine_sim = cosine_similarity(tfidf_1, tfidf_2).mean()
    print('cosine_sim: ', cosine_sim)

path_name_1 = "/Users/andreasalgado/Documents/MIT-MEng/research/pseudo-code-2-code-project/EoH-scripts/original-pseudocode"
path_name_2 = "/Users/andreasalgado/Documents/MIT-MEng/research/pseudo-code-2-code-project/EoH-scripts/amazing-test-done/ReEvo/step-0/generated-pseudocode"
get_vector_matrix(path_name_1, path_name_2)

# original_tfidf = get_vector_matrix("/Users/andreasalgado/Documents/MIT-MEng/research/pseudo-code-2-code-project/EoH-scripts/original-pseudocode")
# generated_tfidf = get_vector_matrix("/Users/andreasalgado/Documents/MIT-MEng/research/pseudo-code-2-code-project/EoH-scripts/generated-pseudocode")

# print('original_tfidf shape:')
# print(original_tfidf.shape)
# cosine_sim_list = [cosine_similarity(original_tfidf[i:i+1], generated_tfidf[0:1]) for i in range(original_tfidf.shape[0])]
# cosine_sim = sum(cosine_sim_list)/len(cosine_sim_list)

# print("cosine similarity: ", cosine_sim)
