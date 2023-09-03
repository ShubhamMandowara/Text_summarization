import streamlit as st
from python_algo import main as python_main
from sumy_lib_based_summary import main as sumy_main


if __name__ == "__main__":
    st.runtime.legacy_caching.clear_cache()
    st.set_page_config(layout="wide")
    st.title("Text Summarization ✍️")
    with st.expander("About this app"):
        st.write(
            "This app is designed by Shubham Mandowara to showcase text summarization using various techniques. You can select the model, and a text summary will be generated at the bottom"
        )
    st.sidebar.header("Select a model from the list 👇🏻:")
    
    st.sidebar.markdown('Follow me on linked to know more about AI, ML, DL, Generative AI, Deployment and MLOps')
    
    with st.sidebar:
        column1, column2 = st.columns(2)
        column1.markdown("[![Linkedin]('https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg')]('https://www.linkedin.com/in/shubhammandowara/')")
        column2.markdown("[![Github]('https://img.icons8.com/material-outlined/48/000000/github.png')]('https://github.com/ShubhamMandowara')")
    model_selection = st.sidebar.selectbox(
        "Choose a model",
        [
            "",
            "Core Python algo(Frequency and Ranking based)",
            "Lex Rank: From Python lib sumy",
            "LSA: From Python lib sumy",
            "Text Rank: From Python lib sumy",
        ],
    )
    st.info('INFO: Ctrl + Enter to get summary OR click anywhere outside once you enter everything', icon="ℹ️")
    text_to_summarize = st.text_area("Enter your text to summarize")
    no_of_sentence_on_output = st.number_input('No. of sentences on output you want', min_value=2, max_value=100)
    st.write("Selected Model:- ", model_selection)
    summary = st.write("Summary:")
    if model_selection != "" and text_to_summarize != "" and no_of_sentence_on_output != None:
        if model_selection == "Core Python algo(Frequency and Ranking based)":
            st.write(python_main(text=text_to_summarize, sentence_on_output=no_of_sentence_on_output))
        elif model_selection == "Lex Rank: From Python lib sumy":
            st.write(sumy_main(text=text_to_summarize, model_name='Lex Rank', sentence_on_output=no_of_sentence_on_output))
        elif model_selection == "LSA: From Python lib sumy":
            st.write(sumy_main(text=text_to_summarize, model_name='LSA', sentence_on_output=no_of_sentence_on_output))
        elif model_selection == "Text Rank: From Python lib sumy":
            st.write(sumy_main(text=text_to_summarize, model_name='Text Rank', sentence_on_output=no_of_sentence_on_output))
        else:
            st.write('Not entering into any condition')
    
    