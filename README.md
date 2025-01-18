## QA with Documents (Information Retrieval) ##

This project is a Generative AI-powered Question and Answer System that retrieves and processes information from uploaded documents to answer user queries. It leverages advanced AI technologies and tools for efficient information retrieval and presents results in a user-friendly Streamlit application.

## Features ##
1. Document-Based Q&A:
* Allows users to upload files (up to 200 MB) for processing.
* Dynamically generates answers to user queries based on the uploaded document's content.
2. AI Model Integration:
* Utilizes the Google Gemini Model (Gemini Pro) for generative AI tasks.
* Built with Llama Index for seamless model integration and document indexing.
* Implements Gemini embeddings for accurate query-response generation.
3. Vector Store Indexing:
* Efficient storage and retrieval of document embeddings using a vector store.
4. Interactive Streamlit Interface:
* Clean and responsive UI for document upload, question submission, and answer visualization.


## Installation and Setup

1. Clone the repository :
   ```bash
   git clone https://github.com/ish-war/qa-with-documents.git
   cd qa-with-documents

2. Install dependencies :
   ```bash
   pip install -r requirements.txt

3. Run the Streamlit app :
   ```bash
   streamlit run app.py

## Dependencies

* Python 3.8+
* Llama Index: Indexing for efficient document-based query retrieval.
* Google Gemini Pro: State-of-the-art generative AI for Q&A.
* Streamlit: Framework for building interactive web apps.
* Additional dependencies listed in requirements.txt.


## Usage

* Open the Streamlit application.
* Upload a document in a supported format (e.g., .txt, .pdf, etc.).
* Enter a query in the input box, and click "Submit & Process."
* View the generated response in the UI.


## Web Interface


![Screenshot 2025-01-18 191119](https://github.com/user-attachments/assets/c00ddc5f-33a9-4a4b-8651-c6456925df77)
