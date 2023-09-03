# imported library
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))

def main(text):
    text = text.lower()
    words = word_tokenize(text)
    word_freq = {} # freq count of words (how many times they came in the text)
    for word in words:
        if word in stop_words:
            continue
        if word in word_freq:
            word_freq[word] += 1 # increase if word came again
        else:
            word_freq[word]  = 1 # if first time add to dict
    
    sentences = sent_tokenize(text) # to create sentence from text
    sentence_ranking = {}
    for sentence in sentences:
        for word, freq in word_freq.items():
            if word in sentence:
                if sentence in sentence_ranking: #increase rank if word in sentence by word frequency
                    sentence_ranking[sentence] += freq
                else:
                    sentence_ranking[sentence] = freq

    rank_sum = 0
    for sentence in sentence_ranking:
        rank_sum += sentence_ranking[sentence]
    avg = int(rank_sum / len(sentence_ranking))
    summary = ''
    for sentence in sentences:
        if sentence_ranking[sentence] > (1.2*avg):
            summary += ' '+ sentence
    return summary