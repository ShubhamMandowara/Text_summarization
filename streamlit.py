import streamlit as st
from python_algo import main as python_main
from sumy_lib_based_summary import main as sumy_main
# from transformers_based_summary import main as transformers_main

if __name__ == "__main__":
    st.runtime.legacy_caching.clear_cache()
    st.set_page_config(layout="wide")
    st.title("Text Summarization ✍️")
    st.sidebar.header(
        "It's time to master Summarization using a variety of models!"
    )
    st.sidebar.subheader("Select a model from the list 👇🏻:")
    model_selection = st.sidebar.selectbox(
        "👇🏻",
        [
            "",
            "Core Python algo(Frequency and Ranking based)",
            "Lex Rank: From Python lib sumy",
            "LSA: From Python lib sumy",
            "Text Rank: From Python lib sumy",
            # "Transformers: Model google/pegasus-xsum"
        ],
    )
    
    st.sidebar.write("----")
    st.sidebar.subheader("About this app:")
    st.sidebar.write(
        "Designed by **Shubham Mandowara** to showcase text summarization using various techniques. You can select the model, and add text to summarize."
    )
    st.sidebar.write("I hope this is helpful. Please feel free to contact me if you have any queries."
    )
    st.sidebar.write("----")
    st.sidebar.subheader(
        "🚀 Follow me for the latest insights on AI, ML, DL, Generative AI, Deployment, and MLOps! Stay ahead of the curve. 📊🤖 #AI #MachineLearning #DeepLearning #Tech"
    )

    with st.sidebar:
        column1, column2 = st.columns(2)
        column1.markdown(
            "[![Linkedin](https://img.icons8.com/material-outlined/48/000000/linkedin.png)](https://www.linkedin.com/in/shubhammandowara/)"
        )
        column2.markdown(
            "[![Github](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/ShubhamMandowara)"
        )

    st.info(
        """**Ctrl + Enter** to get summary OR click anywhere outside the input box after entering text \n
        **Select a model from the left sidebar list**""",
        icon="ℹ️",
    )
    st.write("Youtube : [Dive into the code's secrets in a captivating video journey!](https://youtu.be/s3WQW1Cd8eo?si=nU1dEhFnylqBf345)")

    text_to_summarize = st.text_area("Enter your text to summarize:")
    no_of_sentence_on_output = st.number_input(
        "No. of sentences on output you want", min_value=2, max_value=100
    )
    st.write("Selected Model:- ", model_selection)
    summary = st.write("Summary:")
    if (
        model_selection != ""
        and text_to_summarize != ""
        and no_of_sentence_on_output != None
    ):
        if model_selection == "Core Python algo(Frequency and Ranking based)":
            st.write(
                python_main(
                    text=text_to_summarize, sentence_on_output=no_of_sentence_on_output
                )
            )
        elif model_selection == "Lex Rank: From Python lib sumy":
            st.write(
                sumy_main(
                    text=text_to_summarize,
                    model_name="Lex Rank",
                    sentence_on_output=no_of_sentence_on_output,
                )
            )
        elif model_selection == "LSA: From Python lib sumy":
            st.write(
                sumy_main(
                    text=text_to_summarize,
                    model_name="LSA",
                    sentence_on_output=no_of_sentence_on_output,
                )
            )
        elif model_selection == "Text Rank: From Python lib sumy":
            st.write(
                sumy_main(
                    text=text_to_summarize,
                    model_name="Text Rank",
                    sentence_on_output=no_of_sentence_on_output,
                )
            )
        # elif model_selection == "Transformers: Model google/pegasus-xsum":
        #     st.write(transformers_main(text=text_to_summarize))
        else:
            st.write("Not entering into any condition")
