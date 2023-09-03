from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.tokenizers import Tokenizer
from helper.helper import convert_text_to_lowercase
from streamlit.logger import get_logger
import nltk
from typing import List

nltk.download("punkt")


def common_process(text: str)-> str:
    """Function to convert text to lowercase and convert text to tokens using parser
        Arguments:
            text (str): text to convert
        Returns:
            tokens: token parser
    """
    text = convert_text_to_lowercase(text)
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    return parser

def common_return_process(summary):
    summary = ''
    for sentence in summary:
        summary += " " + sentence
    return summary

def main(text:str, model_name:str, sentence_on_output:int=2) -> str:
    """Main function to summarize the text using sumy lib
        Arguments:
            text (str): text to summarize
            model_name (str): name of the model
            sentence_on_output (int): Number of sentences on output
        Returns:
            str: Summary of text
    """
    summarizer = None
    get_logger.info(model_name)
    if model_name == 'Lex Rank':
        summarizer = LexRankSummarizer()
    elif model_name == 'LSA':
        summarizer = LsaSummarizer()
    elif model_name == 'Text Rank':
        summarizer = TextRankSummarizer()
    else:
        raise 'Wrong model name / Model name is not defined'
    parser = common_process(text=text)
    get_logger.info('parsing is done')
    summary = summarizer(parser.document,sentence_on_output)
    get_logger.info(summary)
    return_text = common_return_process(summary=summary)
    get_logger.info(return_text)
    return return_text

