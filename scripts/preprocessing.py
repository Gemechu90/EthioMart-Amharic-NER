import re
import unicodedata
from typing import Dict, List

def normalize_amharic(text: str) -> str:
    """
    Normalize Amharic text.
    """
    # Convert to NFKC form for consistency
    normalized = unicodedata.normalize('NFKC', text)
    return normalized

def clean_text(text: str) -> str:
    """
    Clean the text by removing unnecessary whitespace, specific patterns, English letters, and emojis.
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove '\n' characters
    text = text.replace('\\n', ' ')
    
    # Remove English letters
    text = re.sub(r'[a-zA-Z]', '', text)

    # Remove emojis 
    #text = re.sub(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF]', '', text)
    text = re.sub(
    r'['
    r'\U0001F600-\U0001F64F'  # Emoticons
    r'\U0001F300-\U0001F5FF'  # Symbols & Pictographs
    r'\U0001F680-\U0001F6FF'  # Transport & Map symbols
    r'\U0001F700-\U0001F77F'  # Alchemical symbols
    r'\U0001F780-\U0001F7FF'  # Geometric shapes extended
    r'\u0031\uFE0F\u20E3'     # Unicode for 1️⃣ (digit one with keycap)
    r']', 
    '', 
    text
)
    return text


def tokenize_mixed_text(text: str) -> List[str]:
    """
    Tokenize text that contains both Amharic and English.
    """
    #  simple tokenization.
    return text.split()

def preprocess_message(message: Dict[str, any]) -> Dict[str, any]:
    """
    Preprocess a single message.
    """
    # Normalize and clean the message text
    cleaned_message = clean_text(normalize_amharic(message['Message']))
    
    return {
        'Channel_Title': message['Channel Title'],
        'Channel_Username': message['Channel Username'],
        'ID': message['ID'],
        'cleaned_message': cleaned_message,
        'tokens': tokenize_mixed_text(cleaned_message),
        'Date': message['Date'],
        'Media_Path': message['Media Path']
    }

def preprocess_dataset(dataset: List[Dict[str, any]]) -> List[Dict[str, any]]:
    """
    Preprocess the entire dataset.
    """
    return [preprocess_message(message) for message in dataset]