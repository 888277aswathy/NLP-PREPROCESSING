# Import necessary libraries
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Function to perform tokenization with spaCy
def spacy_tokenization(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    tokens_spacy = [token.text for token in doc if not token.is_punct and not token.is_space]
    return tokens_spacy

# Function to perform stemming with spaCy (spaCy does not have built-in stemming, so we use lemmatization as a substitute)
def spacy_stemming(words):
    nlp = spacy.load("en_core_web_sm")
    stemmed_words_spacy = [token.lemma_ for token in nlp(" ".join(words))]
    return stemmed_words_spacy

# Function to perform lemmatization with spaCy
def spacy_lemmatization(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    lemmatized_words_spacy = [token.lemma_ for token in doc if not token.is_punct and not token.is_space]
    return lemmatized_words_spacy

# Function to remove stopwords with spaCy
def spacy_remove_stopwords(words):
    nlp = spacy.load("en_core_web_sm")
    tokens_without_stopwords = [token.text for token in nlp(" ".join(words)) if not token.is_stop and not token.is_punct and not token.is_space]
    return tokens_without_stopwords

# Main function for user interaction
def main():
    print("Welcome to Text Processing with spaCy!")
    print("Enter the text you want to process:")
    text = input()
    
    # spaCy tokenization
    tokens_spacy = spacy_tokenization(text)
    
    # spaCy stemming (using lemmatization as a substitute)
    stemmed_words_spacy = spacy_stemming(tokens_spacy)
    
    # spaCy lemmatization
    lemmatized_words_spacy = spacy_lemmatization(text)
    
    # spaCy stopword removal
    tokens_without_stopwords_spacy = spacy_remove_stopwords(tokens_spacy)
    
    # Print spaCy results
    print("\nTokenization with spaCy:")
    print(tokens_spacy)
    print("\nStemming (using lemmatization) with spaCy:")
    print(stemmed_words_spacy)
    print("\nLemmatization with spaCy:")
    print(lemmatized_words_spacy)
    print("\nStopwords Removed with spaCy:")
    print(tokens_without_stopwords_spacy)

# Execute the main function
if __name__ == "__main__":
    main()
