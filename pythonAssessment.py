# pythonAssessment.py

import re
from collections import Counter


def read_news_article(file_name):
    """
    Read the contents of a text file and return it as a string.
    Returns an empty string if the file cannot be read.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return ""
    except OSError as error:
        print(f"Error reading file: {error}")
        return ""


def extract_words(text):
    """
    Extract words from text while excluding punctuation and special characters.
    Returns a list of lowercase words.
    """
    return re.findall(r"\b[a-zA-Z0-9']+\b", text.lower())


def count_specific_word(text, search_word):
    """
    Count the number of occurrences of a specific word in the text.
    Returns an integer.
    Edge case: if no matches are found, returns 0.
    """
    if not text or not search_word.strip():
        return 0

    pattern = r"\b" + re.escape(search_word.lower()) + r"\b"
    matches = re.findall(pattern, text.lower())
    return len(matches)


def identify_most_common_word(text):
    """
    Identify the most common word in the text.
    Returns the word as a string.
    Edge case: empty string returns None.
    """
    words = extract_words(text)

    if not words:
        return None

    word_counts = Counter(words)
    return word_counts.most_common(1)[0][0]


def calculate_average_word_length(text):
    """
    Calculate the average length of words in the text.
    Excludes punctuation marks and special characters.
    Returns a float.
    Edge case: empty string returns 0.
    """
    words = extract_words(text)

    if not words:
        return 0

    total_length = sum(len(word) for word in words)
    return total_length / len(words)


def count_paragraphs(text):
    """
    Count the number of paragraphs in the text.
    Paragraphs are separated by empty lines.
    Returns an integer.
    Edge case: empty string returns 1.
    """
    if not text.strip():
        return 1

    paragraphs = re.split(r"\n\s*\n", text.strip())
    return len(paragraphs)


def count_sentences(text):
    """
    Count the number of sentences in the text.
    Sentences are defined by periods, exclamation marks, and question marks.
    Returns an integer.
    Edge case: empty string returns 1.
    """
    if not text.strip():
        return 1

    # Protect common abbreviations so their periods do not split sentences
    abbreviations = [
        "Mr.", "Mrs.", "Ms.", "Dr.", "Prof.", "Inc.", "Ltd.",
        "Jr.", "Sr.", "St.", "e.g.", "i.e."
    ]

    protected_text = text
    for abbreviation in abbreviations:
        protected_text = protected_text.replace(abbreviation, abbreviation.replace(".", "<DOT>"))

    sentences = re.split(r"[.!?]+", protected_text)
    valid_sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    return len(valid_sentences)


def display_results(text, search_word):
    """
    Run all text analysis functions and display results.
    """
    specific_word_count = count_specific_word(text, search_word)
    most_common_word = identify_most_common_word(text)
    average_word_length = calculate_average_word_length(text)
    paragraph_count = count_paragraphs(text)
    sentence_count = count_sentences(text)

    print("\n--- News Article Text Analysis Results ---")
    print(f"Specific word searched: '{search_word}'")
    print(f"Count of '{search_word}': {specific_word_count}")
    print(f"Most common word: {most_common_word}")
    print(f"Average word length: {average_word_length:.2f}")
    print(f"Number of paragraphs: {paragraph_count}")
    print(f"Number of sentences: {sentence_count}")


def main():
    """
    Main program execution.
    """
    file_name = input("Enter the name of the news article text file: ").strip()
    article_text = read_news_article(file_name)

    if not article_text:
        print("No article text available for analysis.")
        return

    search_word = input("Enter the specific word to count: ").strip()
    display_results(article_text, search_word)


if __name__ == "__main__":
    main()