# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from gensim.parsing.preprocessing import preprocess_string

# Function to perform tokenization with NLTK
def nltk_tokenization(text):
    words_nltk = word_tokenize(text)
    return words_nltk

# Function to perform stemming with NLTK
def nltk_stemming(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

# Function to perform lemmatization with NLTK
def nltk_lemmatization(words):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return lemmatized_words

# Function to remove stopwords with NLTK
def nltk_remove_stopwords(words):
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return filtered_words

# Main function for user interaction
def main():
    print("Welcome to Text Processing with NLTK and Gensim!")
    print("Enter the text you want to process:")
    text = input()
    
    # NLTK tokenization
    words_nltk = nltk_tokenization(text)
    
    # NLTK stemming
    stemmed_words_nltk = nltk_stemming(words_nltk)
    
    # NLTK lemmatization
    lemmatized_words_nltk = nltk_lemmatization(words_nltk)
    
    # NLTK stopword removal
    filtered_words_nltk = nltk_remove_stopwords(words_nltk)
    
    # Gensim simple preprocessing (basic tokenization)
    tokens_gensim = preprocess_string(text)
    
    # Print NLTK results
    print("\nNLTK Word Tokenization:")
    print(words_nltk)
    print("\nNLTK Stemmed Words:")
    print(stemmed_words_nltk)
    print("\nNLTK Lemmatized Words:")
    print(lemmatized_words_nltk)
    print("\nNLTK Stopwords Removed:")
    print(filtered_words_nltk)
    
    # Print Gensim results (basic tokenization)
    print("\nGensim Simple Preprocessing (Tokenization):")
    print(tokens_gensim)

# Execute the main function
if __name__ == "__main__":
    main()
