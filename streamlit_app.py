import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model

def main():
    st.set_page_config(page_title="QA with Documents")

    st.header("QA with Documents (Information Retrieval)")

    # Allow multiple file uploads (PDF, TXT, DOCX)
    uploaded_files = st.file_uploader(
        "Upload your documents (PDF, TXT, DOCX only)",
        type=["pdf", "txt", "docx"],
        accept_multiple_files=True
    )

    user_question = st.text_input("Ask your question")

    if st.button("Submit & Process"):
        if not uploaded_files:
            st.warning("Please upload at least one document.")
            return
        
        with st.spinner("Processing..."):
            all_documents = []
            
            # Process each uploaded document
            for uploaded_file in uploaded_files:
                document = load_data(uploaded_file)
                all_documents.extend(document)
            
            # Load model and create query engine
            model = load_model()
            query_engine = download_gemini_embedding(model, all_documents)

            # Get response
            response = query_engine.query(user_question)

            # Display answer
            if response.response.strip():
                st.write(response.response)
            else:
                st.write("The provided documents do not contain any information about your question.")

if __name__ == "__main__":
    main()
