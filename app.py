import streamlit as st
from src.rag_pipeline import indexing_pipeline, get_answer


from dotenv import load_dotenv
import os
load_dotenv()

st.set_page_config(page_title="HR Policy Assistant", page_icon=":robot_face:", layout="centered")
st.title("HR Policy Assistant Chatbot")

# Upload Document
uploaded_file = st.file_uploader("Upload the HR policy document", type=["pdf"], key="file_uploader")

if uploaded_file is not None:
    file_path = f"data/sample_pdfs/{uploaded_file.name}"
    with open(file_path,"wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("File uploaded successfully!")

    if st.button("Ingest/Process Document"):
        with st.spinner("Processing document..."):
            indexing_pipeline(file_path)
        st.success("Document processed and indexed successfully!")

# Question Answering
st.subheader("Ask a question about the HR policies")

# streamlit text input for question
question = st.text_input("Enter your question here", key="question_input")
# question = st.text_area("Enter your question here", key="question_input")


# provide button to get answer
if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Getting answer..."):
            answer = get_answer(question)
        st.markdown(f"**Answer:** {answer}")