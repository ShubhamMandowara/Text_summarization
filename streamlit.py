import streamlit as st
from python_algo import main

if __name__ == '__main__':
    st.runtime.legacy_caching.clear_cache()
    st.set_page_config(layout='wide')
    st.title('Text Summarization ✍️')
    with st.expander('About this app'):
        st.write('This app is designed to showcase text summarization using various techniques. You can select the model, and a text summary will be generated at the bottom')
    st.sidebar.header('Select a model from the list 👇🏻:')
    model_selection = st.sidebar.selectbox('Chose a model', ['', 'Core Python algo(Frequency and Ranking based)', 'Python lib sumy: lax', 'Python lib sumy: textrank'])

    text_to_summarize = st.text_area('Enter your text to summarize')

    summary = st.write('Summary: ')

    if model_selection != '' and text_to_summarize != '':
        if model_selection  == 'Core Python algo(Frequency and Ranking based)':
            st.write('frequncy and ranking based python model')
            st.write(main(text=text_to_summarize))
        if model_selection  == 'Python lib sumy: lax':
            st.write('In progerss')
        if model_selection  == 'Python lib sumy: textrank':
            st.write('In progerss')
