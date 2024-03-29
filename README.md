# ChatPDF: Interactive Document Conversational Interface

[ChatPDF](https://samsonbakos-chatpdf.streamlit.app) is a Streamlit-based web application designed to facilitate interactive querying of PDF documents.

## Features

- **PDF Text Extraction**: Utilizes PyMuPDF (fitz) to accurately extract text from uploaded PDF documents, ensuring that the full content is available for querying.
- **Natural Language Querying**: Integrates OpenAI's language models via LangChain to understand and respond to user queries in natural language, making document exploration intuitive and efficient.
- **Adaptive Text Chunking**: Implements a recursive function to split document text into manageable chunks. This method ensures that large documents are processed effectively, enhancing the model's ability to provide accurate and relevant responses.
- **Intelligent Summarization**: To avoid repetitive or fragmented responses from individual text chunks, the app employs a summarization step. This step consolidates responses into a single, coherent answer, enhancing user experience by providing clear and concise information.
- **Streamlit Interface**: Offers a user-friendly web interface built with Streamlit, enabling easy upload of PDF files and seamless interaction with the document content through natural language queries.

## How It Works

1. **Upload a PDF**: Users start by uploading a PDF document through the Streamlit interface.
2. **Extract Text**: The application extracts text from the PDF using PyMuPDF, displaying the extracted content for user reference.
3. **Enter Queries**: Users can then enter natural language queries regarding the content of the uploaded document.
4. **Receive Answers**: The app processes the document text in chunks, queries OpenAI's language models for each chunk, and then summarizes the responses to provide a clear and concise answer to the user's question.

## Local Setup and Usage

- Ensure you have Python and Streamlit installed.
- Install the required Python packages, see the [requirements](requirements.txt)
- Run the app locally using Streamlit: `streamlit run src/app.py`.
- For deployment, refer to Streamlit Sharing documentation to securely manage and deploy your application with sensitive API keys hidden.

## License

[MIT License](LICENSE.txt)

## Acknowledgements

- [OpenAI](https://openai.com/) 
- [LangChain](https://github.com/LangChain/langchain) 
- [PyMuPDF](https://pymupdf.readthedocs.io/) 
