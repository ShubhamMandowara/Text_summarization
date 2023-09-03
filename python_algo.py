# imported library
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from helper.helper import convert_text_to_lowercase

nltk.download("stopwords")
nltk.download("punkt")
stop_words = set(stopwords.words("english"))


def main(text, sentence_on_output) -> str:
    """Main function to summarize the text using python based rank and frequency count of words
    Arguments:
        text (str): text to summarize
        sentence_on_output (int): Number of sentences on output
    Returns:
        str: Summary of text
    """
    text = convert_text_to_lowercase(text=text)
    words = word_tokenize(text)
    word_freq = {}  # freq count of words (how many times they came in the text)
    for word in words:
        if word in stop_words:
            continue
        if word in word_freq:
            word_freq[word] += 1  # increase if word came again
        else:
            word_freq[word] = 1  # if first time add to dict

    sentences = sent_tokenize(text)  # to create sentence from text
    sentence_ranking = {}
    for sentence in sentences:
        for word, freq in word_freq.items():
            if word in sentence:
                if (
                    sentence in sentence_ranking
                ):  # increase rank if word in sentence by word frequency
                    sentence_ranking[sentence] += freq
                else:
                    sentence_ranking[sentence] = freq

    rank_sum = 0
    for sentence in sentence_ranking:
        rank_sum += sentence_ranking[sentence]
    avg = int(rank_sum / len(sentence_ranking))
    summary = ""
    count = 0
    for sentence in sentences:
        if sentence_ranking[sentence] > (1.2 * avg):
            summary += " " + sentence
            count += 1
        if count == sentence_on_output:
            return summary
    return summary
