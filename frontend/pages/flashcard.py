import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="Flashcards")
st.header("Active Recall")

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text

def main():
    source_material = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
    if st.button("Submit & Process"):
        with st.spinner("Processing..."):
            try:
                raw_text = get_pdf_text(source_material)
                st.success("PDF Processed Successfully")
            except:
                st.error("Processing failed")

        no_of_questions = st.number_input("no of questions expected")

        if st.button("Generate Flash cards"):
            pass

if __name__ == "__main__":
    main()