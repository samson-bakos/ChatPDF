import fitz
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate


def split_text_recursive(text, max_length=1024):
    """Splits text into chunks that are smaller than max_length handling edge cases."""
    if len(text) <= max_length:
        return [text]
    else:
        # suitable split point (e.g., end of a sentence)
        split_point = text.rfind(". ", 0, max_length) + 1
        if split_point <= 0:  # no suitable split point, force split at max_length
            split_point = max_length
        return [text[:split_point]] + split_text_recursive(
            text[split_point:], max_length
        )


def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file using PyMuPDF."""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def query_llm(text_chunks, query, llm):
    """Queries the loaded LLM with the chunked text and the user query
    Also resummarizes with a second llm query to prevent repeated responses
    as each chunk generates a response"""
    combined_responses = []
    for chunk in text_chunks:
        full_query = f"{query} {chunk}"
        template = PromptTemplate.from_template("Question: {question}\n\nAnswer:")

        llm_chain = LLMChain(prompt=template, llm=llm)
        response = llm_chain.run({"question": full_query})

        if hasattr(response, "text"):
            response_text = response.text.strip()
            combined_responses.append(response_text)
        elif isinstance(response, str):
            combined_responses.append(response.strip())

    # Join the responses into a single text block for summarization
    combined_text = " ".join(combined_responses)

    # Make a new query to the model for summarization
    summary_prompt = (
        f"Summarize the following responses into a concise answer: {combined_text}"
    )
    summary_response = llm_chain.run({"question": summary_prompt})

    final_summary = (
        summary_response.text.strip()
        if hasattr(summary_response, "text")
        else summary_response
    )
    return final_summary
