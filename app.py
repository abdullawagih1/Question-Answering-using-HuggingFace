import streamlit as st
from transformers import pipeline

# Get model
model = pipeline("question-answering")

st.title("Ask Questions about your Text")
sentence = st.text_area('Please paste your article :', height=30)
question = st.text_input("Questions from this article?")
button = st.button("Get me Answers")
with st.spinner("Discovering Answers.."):
    if button and sentence:
        answers = model(question=question, context=sentence)
        st.write(answers['answer'])