from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.tokenizers import Tokenizer
from helper.helper import convert_text_to_lowercase
import nltk
from typing import List

nltk.download("punkt")


def common_process(text: str):
    """Function to convert text to lowercase and convert text to tokens using parser
        Arguments:
            text (str): text to convert
        Returns:
            tokens: token parser
    """
    text = convert_text_to_lowercase(text)
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    return parser

def common_return_process(summary:List):
    summary = ''
    for sentence in summary:
        summary += " " + sentence
    return summary

def main(text, model_name, sentence_on_output:int=2) -> str:
    """Main function to summarize the text using sumy lib
        Arguments:
            text (str): text to summarize
            sentence_on_output (int): Number of sentences on output
        Returns:
            str: Summary of text
    """
    summarizer = None
    if model_name == 'Lex Rank':
        summarizer = LexRankSummarizer()
    elif model_name == 'LSA':
        summarizer = LsaSummarizer()
    elif model_name == 'Text Rank':
        summarizer = TextRankSummarizer()
    else:
        raise 'Wrong model name / Model name is not defined'
    parser = common_process(text=text)
    summary = summarizer(parser.document,sentence_on_output)
    return_text = common_return_process(summary=summary)
    print(return_text)
    return return_text

