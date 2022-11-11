import nltk
import re
from nltk.stem.snowball import SnowballStemmer


def tokenize_and_stem(text):
    
    """
    This function Tokenizes and stems the text that is input
    
    params:
    
    text (string): The text we want to tokenize and stem
    
    returns:
    
    stems (list): The list of stemmed and tokenized words
    
    """
    
    stemmer = SnowballStemmer("english")
    
    # Tokenize by sentence, then by word
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    
    # Filter out raw tokens to remove noise
    filtered_tokens = [token for token in tokens if re.search('[a-zA-Z]', token)]
    
    # Stem the filtered_tokens
    stems = [stemmer.stem(t) for t in filtered_tokens]
    
    return stems