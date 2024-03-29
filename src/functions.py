import fitz


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from PDF
    """
    pdf_text = ""
    pdf_document = fitz.open(uploaded_file)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pdf_text += page.get_text()
    return pdf_text


def process_query(query, pdf_text):
    """
    Uses LangChain to parse a query
    """
    lc = langchain.LangChain()
    lc.train(pdf_text)
    response = lc.process(query)
    return response
