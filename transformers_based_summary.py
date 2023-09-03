# from transformers import PegasusForConditionalGeneration, PegasusTokenizer, pipeline

# model_name = 'google/pegasus-xsum'
# pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name) # tokenizer of model
# pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

# def main(text):
#     summarizer = pipeline(
#             "summarization",
#             model=model_name,
#             tokenizer=pegasus_tokenizer,
#             framework='pt',
#         )
#     summary = summarizer(text, min_length=30, max_length=150)
#     return summary[0]
    